from odoo import models, fields
from ..services.dnd_api_service import DndApiService
import logging

_logger = logging.getLogger(__name__)


class OdoomancyMonsterImporter(models.TransientModel):
    _name = "odoomancy.monster.importer"
    _description = "Odoomancy Monster Importer"

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

    def action_import_monsters(self):
        api = DndApiService()

        monster_list = api.list_monsters()
        results = monster_list.get("results", [])

        indexes = [m["index"] for m in results]

        existing_monsters = self.env["odoomancy.monster"].search(
            [("name", "in", indexes)]
        )
        existing_by_index = {m.name: m for m in existing_monsters}

        to_create = []
        to_update = []
        errors = 0

        for monster_ref in results:
            try:
                monster_data = api.get_monster(monster_ref["index"])

                vals = {
                    "api_index": monster_ref.get("index"),
                    "name": monster_data.get("name"),
                    "size": monster_data.get("size"),
                    "type": monster_data.get("type"),
                    "alignment": monster_data.get("alignment"),
                    "hit_points": monster_data.get("hit_points"),
                    "challenge_rating": monster_data.get("challenge_rating"),
                }

                existing = existing_by_index.get(monster_ref["index"])

                if existing:
                    if self.import_mode == "upsert":
                        to_update.append((existing, vals))
                else:
                    to_create.append(vals)

            except Exception:
                errors += 1
                _logger.exception("Error importing monster %s", monster_ref.get("index"))

        self.env["odoomancy.monster"].create(to_create)

        for record, vals in to_update:
            record.write(vals)

        self.created_count = len(to_create)
        self.updated_count = len(to_update)
        self.error_count = errors

        return {
            "type": "ir.actions.act_window",
            "res_model": "odoomancy.monster.importer",
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
        }