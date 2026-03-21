from odoo import models
from ...services.dnd_api_service import DndApiService


class OdoomancySkillImporter(models.TransientModel):
    _name = "odoomancy.skills.importer"
    _inherit = "odoomancy.importer.mixin"

    _description = "Imports skills of each ability_score."

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.skill"

    def _get_api_list(self, api):
        return [{"index":key} for key, _ in self.env['odoomancy.skill']._fields['name'].selection]

    def _get_api_detail(self, api, ref):
        skills = api.list_(f'skills/{ref}')
        return skills

    def _map_api_to_vals(self, data):
        index = data.get('index')
        desc = data.get("desc") or data.get("description") or []
        description = "<br/>".join(desc) if isinstance(desc, list) else desc or ""
        ability_score = None
        if "ability_score" in data and "index" in data.get("ability_score"):
            ability_score = data.get("ability_score").get("index")
            ability_score = self.env['odoomancy.ability.scores'].search([('name', '=', ability_score)], limit=1)

        return{
            "name": index,
            "api_index": index,
            "description": description,
            "ability_score_ids": ability_score if ability_score else None,
        }

    def _get_external_key(self, ref, data):
        return ref.get('index')