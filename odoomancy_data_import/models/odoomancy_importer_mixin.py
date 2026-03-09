from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class OdoomancyImporterMixin(models.AbstractModel):
    _name = "odoomancy.importer.mixin"
    _description = "Generic API Importer Mixin"

    import_mode = fields.Selection(
        [
            ("create_only", "Create Only"),
            ("upsert", "Create or Update"),
        ],
        default="upsert",
        required=True,
    )

    created_count = fields.Integer(readonly=True)
    updated_count = fields.Integer(readonly=True)
    error_count = fields.Integer(readonly=True)

    # ----- METHODS TO OVERRIDE -----

    def _get_model_name(self):
        """Must return the name of the target model"""
        raise NotImplementedError()

    def _get_api_list(self, api):
        """Must return a list of references"""
        raise NotImplementedError()

    def _get_api_detail(self, api, ref):
        """Must return the details of an item"""
        raise NotImplementedError()

    def _map_api_to_vals(self, data):
        """Must transform JSON into Odoo values"""
        raise NotImplementedError()

    def _get_external_key(self, ref, data):
        """‘Unique external key (e.g., index)"""
        raise NotImplementedError()

    # ----- GENERIC LOGIC -----

    def action_import(self):
        api = self._get_api_service()
        model = self.env[self._get_model_name()]

        refs = self._get_api_list(api)

        external_keys = [r["index"] for r in refs]

        existing = model.search([("api_index", "in", external_keys)])
        existing_map = {rec.api_index: rec for rec in existing}

        to_create = []
        to_update = []
        errors = 0

        for ref in refs:
            try:
                data = self._get_api_detail(api, ref["index"])
                vals = self._map_api_to_vals(data)
                external_key = self._get_external_key(ref, data)

                record = existing_map.get(external_key)

                if record:
                    if self.import_mode == "upsert":
                        with self.env.cr.savepoint():
                            record.write(vals)
                            print("Updated:", record.name)
                else:
                    with self.env.cr.savepoint():
                        model.create([vals])
                        print("Create:", vals.get("name", external_key))

            except Exception:
                errors += 1
                _logger.exception("Error importing %s", ref.get("index"))
                continue

        self.error_count = errors

        return self._reload_wizard()

    def _reload_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": self._name,
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
        }