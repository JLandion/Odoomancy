
from odoo import models
from ...services.dnd_api_service import DndApiService


class OdoomancyProficienceImporter(models.TransientModel):
    _name = "odoomancy.proficience.importer"
    _inherit = "odoomancy.importer.mixin"

    _description = "Imports Proficiencies."

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.proficience"

    def _get_api_list(self, api):
        return api.list_('proficiencies').get("results", [])

    def _get_api_detail(self, api, ref):
        return api.get_('proficiencies', ref)

    def _map_api_to_vals(self, data):
        name = data.get("name")
        api_index = data.get("index")
        type = data.get('type')

        if "class" in data and "index" in data.get("classes"):
            class_ = data.get("classes").get("index")
            class_ = self.env['odoomancy.class'].search([('type', '=', class_)], limit=1)
        else:
            class_ = self.env['odoomancy.class'].search([])
        return {
                "name": name,
                "api_index": api_index,
                "class_id": class_,
                "type": type,
            }

    def _get_external_key(self, ref, data):
        return ref.get("index")