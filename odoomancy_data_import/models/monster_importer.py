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

        created = 0
        updated = 0
        errors = 0

        monster_list = api.list_monsters()

        for monster_ref in monster_list.get("results", [])[:20]:
            try:
                monster_data = api.get_monster(monster_ref["index"])
                result = self._upsert_monster(monster_data)

                if result == "created":
                    created += 1
                elif result == "updated":
                    updated += 1

            except Exception:
                errors += 1
                _logger.exception(
                    "Error importing monster %s", monster_ref.get("index")
                )

        self.created_count = created
        self.updated_count = updated
        self.error_count = errors

        return {
            "type": "ir.actions.act_window",
            "res_model": "odoomancy.monster.importer",
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
        }

    def _upsert_monster(self, monster_data):
        Monster = self.env["odoomancy.monster"]

        existing = Monster.search(
            [("name", "=", monster_data["index"])],
            limit=1,
        )

        vals = {
            "name": monster_data.get("name"),
            "size": monster_data.get("size"),
            "type": monster_data.get("type"),
            "alignment": monster_data.get("alignment"),
            "hit_points": monster_data.get("hit_points"),
            "challenge_rating": monster_data.get("challenge_rating"),
        }

        if existing:
            if self.import_mode == "upsert":
                existing.write(vals)
                return "updated"
            return "skipped"

        Monster.create(vals)
        return "created"