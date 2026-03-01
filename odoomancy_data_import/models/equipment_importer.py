from odoo import models
from ..services.dnd_api_service import DndApiService


class OdoomancyEquipmentImporter(models.TransientModel):
    _name = "odoomancy.equipment.importer"
    _inherit = "odoomancy.importer.mixin"

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.equipment"

    def _get_api_list(self, api):
        return api.list_equipment().get("results", [])

    def _get_api_detail(self, api, ref):
        return api.get_equipment(ref)

    def _map_api_to_vals(self, data):
        return {
            "api_index": data.get("index"),
            "name": data.get("name"),
            "size": data.get("size"),
            "type": data.get("type"),
            "alignment": data.get("alignment"),
            "hit_points": data.get("hit_points"),
            "challenge_rating": data.get("challenge_rating"),
        }

    def _get_external_key(self, ref, data):
        return data.get("index")