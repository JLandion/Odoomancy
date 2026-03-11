from odoo import models, fields, api
import logging
import threading

_logger = logging.getLogger(__name__)
_import_stop_events = {}


class OdoomancyImporterMixin(models.AbstractModel):
    _name = "odoomancy.importer.mixin"
    _description = "Generic API Importer Mixin"

    import_mode = fields.Selection(
        [("create_only", "Create Only"), ("upsert", "Create or Update")],
        default="upsert",
        required=True,
    )

    progress = fields.Integer(string="Progress", default=0)
    progress_label = fields.Char(string="Status")
    is_running = fields.Boolean(string="Is Running", default=False)

    # ----- METHODS TO OVERRIDE -----

    def _get_api_service(self):
        raise NotImplementedError()

    def _get_model_name(self):
        raise NotImplementedError()

    def _get_api_list(self, api):
        raise NotImplementedError()

    def _get_api_detail(self, api, ref):
        raise NotImplementedError()

    def _map_api_to_vals(self, data):
        raise NotImplementedError()

    def _get_external_key(self, ref, data):
        raise NotImplementedError()

    # ----- AUX METHODS -----

    def _selection_label_to_key(self, model, field_name, label):
        if not label:
            return False

        selection = dict(self.env[model]._fields[field_name].selection)
        reverse_selection = {v: k for k, v in selection.items()}

        return reverse_selection.get(label)
    # ----- GENERIC LOGIC -----

    def action_import(self):
        self.write({"progress": 0, "progress_label": "Starting...", "is_running": True})
        self.env.cr.commit()

        wizard_id = self.id
        dbname = self.env.cr.dbname
        uid = self.env.uid
        context = dict(self.env.context)
        importer_model = self.importer_model

        stop_event = threading.Event()
        _import_stop_events[wizard_id] = stop_event

        thread = threading.Thread(
            target=self._run_import_thread,
            args=(dbname, uid, context, wizard_id, importer_model, stop_event),
            daemon=True,
        )
        thread.start()

        return self._reload_wizard()

    def _run_import_thread(self, dbname, uid, context, wizard_id, importer_model, stop_event):
        from odoo.modules.registry import Registry
        with Registry(dbname).cursor() as cr:
            env = api.Environment(cr, uid, context)
            wizard = env[self._name].browse(wizard_id)
            try:
                sub_importer = env[importer_model].create([{
                    "import_mode": wizard.import_mode,
                }])

                sub_importer._do_import_into(env, stop_event, wizard)
            except Exception:
                _logger.exception("Import thread failed")
                wizard.write({"is_running": False, "progress_label": "Error"})
                cr.commit()
            finally:
                _import_stop_events.pop(wizard_id, None)

    def _do_import_into(self, env, stop_event, progress_wizard):
        """
        Ejecuta la importación pero reporta el progreso
        en `progress_wizard` en lugar de en `self`.
        Esto permite que el wizard global muestre el progreso
        aunque el que importa sea el sub-importer.
        """
        api_service = self._get_api_service()
        model = env[self._get_model_name()]

        refs = self._get_api_list(api_service)
        total = len(refs)

        external_keys = [r["index"] for r in refs]
        existing = model.search([("api_index", "in", external_keys)])
        existing_map = {rec.api_index: rec for rec in existing}

        for i, ref in enumerate(refs):
            if stop_event.is_set():
                _logger.info("Import cancelled at %s/%s", i, total)
                progress_wizard.write({
                    "is_running": False,
                    "progress_label": f"Cancelled at {i} / {total}",
                })
                env.cr.commit()
                return

            try:
                data = self._get_api_detail(api_service, ref["index"])
                vals = self._map_api_to_vals(data)
                external_key = self._get_external_key(ref, data)
                record = existing_map.get(external_key)

                if record:
                    if progress_wizard.import_mode == "upsert":
                        with env.cr.savepoint():
                            record.write(vals)
                else:
                    with env.cr.savepoint():
                        model.create([vals])

                progress_wizard.write({
                    "progress": int((i + 1) / total * 100),
                    "progress_label": f"{i + 1} / {total}",
                })
                env.cr.commit()

            except Exception:
                _logger.exception("Error importing %s", ref.get("index"))
                continue

        progress_wizard.write({
            "is_running": False,
            "progress": 100,
            "progress_label": f"Done — {total} records",
        })
        env.cr.commit()

    def action_stop(self):
        stop_event = _import_stop_events.get(self.id)
        if stop_event:
            stop_event.set()

    def action_get_progress(self):
        return {
            "progress": self.progress,
            "progress_label": self.progress_label,
            "is_running": self.is_running,
        }

    def _reload_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": self._name,
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
        }