from odoo import models
from ..services.dnd_api_service import DndApiService


class OdoomancyClassImporter(models.TransientModel):
    _name = "odoomancy.class.importer"
    _inherit = "odoomancy.importer.mixin"

    _description = "Import Classes from D&D Api"

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.class"

    def _get_api_list(self, api):
        return api.list_('classes').get("results", [])

    def _get_api_detail(self, api, ref):
        return api.get_('classes', ref)

    def _map_api_to_vals(self, data):
        name = data.get("name")
        desc = data.get("desc") or data.get("description") or []
        description = "<br/>".join(desc) if isinstance(desc, list) else desc or ""
        type = data.get('index')
        api_index = data.get('api_index')
        hit_die = data.get('hit_die')

        return {
            "name": name,
            "api_index": api_index,
            "description": description,
            "type": type,
            "hit_die": hit_die,
        }

    def _get_external_key(self, ref, data):
        return data.get("index")