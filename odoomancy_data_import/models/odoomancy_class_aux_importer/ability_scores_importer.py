from odoo import models
from ...services.dnd_api_service import DndApiService


class OdoomancyAbilityScoresImporter(models.TransientModel):
    _name = "odoomancy.ability.scores.importer"
    _inherit = "odoomancy.importer.mixin"

    _description = "Imports Ability Scores."

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.ability.scores"

    def _get_api_list(self, api):
        return [{"index":key} for key, _ in self.env['odoomancy.ability.scores']._fields['name'].selection]

    def _get_api_detail(self, api, ref):
        skills = api.list_(f'ability-scores/{ref}')
        return skills

    def _map_api_to_vals(self, data):
        index = data.get('index')
        desc = data.get("desc") or data.get("description") or []
        description = "<br/>".join(desc) if isinstance(desc, list) else desc or ""

        skills = None
        if "skills" in data and "index" in data.get("skills"):
            skills = data.get("skills").get("index")
            skills = self.env['odoomancy.skills'].search([('name', '=', skills)], limit=1)

        class_ = None
        if "class" in data and "index" in data.get("skills"):
            class_ = data.get("skills").get("index")
            class_ = self.env['odoomancy.skills'].search([('name', '=', class_)], limit=1)

        return{
            "name": index,
            "api_index": index,
            "description": description,
            "skill_id": skills,
            "class_ids": class_,
        }

    def _get_external_key(self, ref, data):
        return ref.get('index')