from odoo import models
from ..services.dnd_api_service import DndApiService


class OdoomancyTraitsImporter(models.Model):
    _name = 'odoomancy.traits.importer'
    _inherit = "odoomancy.importer.mixin"
    _description = 'Odoomancy Traits Importer'

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.traits"

    def _get_api_list(self, api):
        return api.list_('traits').get("results", [])

    def _get_api_detail(self, api, ref):
        return api.get_('traits', ref)

    def _map_api_to_vals(self, data):
        name = data.get('name', "")
        api_index = data.get("index", "")
        desc = data.get("desc") or []
        description = "\n".join(desc) if isinstance(desc, list) else desc or None

        races = []
        if "races" in data and len(data.get('races')) > 0:
            races = [r.get('name') for r in data.get("races")]
            races = self.env['odoomancy.race'].search([('name', 'in', races)])

        subraces = []
        if "subraces" in data and len(data.get('subraces')) > 0:
            subraces = [r.get('name') for r in data.get("subraces")]
            subraces = self.env['odoomancy.subrace'].search([('name', 'in', subraces)])

        proficiencies = []
        if "proficiencies" in data and len(data.get('proficiencies')) > 0:
            proficiencies = [r.get('name') for r in data.get("proficiencies")]
            proficiencies = self.env['odoomancy.proficience'].search([('name', 'in', proficiencies)])

        return {
            "name": name,
            "api_index": api_index,
            "description": description,
            "races": [(6, 0, races.ids)] if len(races) > 0 else False,
            "subraces": [(6, 0, subraces.ids)] if len(subraces) > 0 else False,
            "proficiencies": [(6, 0, proficiencies.ids)] if len(proficiencies) > 0 else False,
        }

    def _get_external_key(self, ref, data):
        return data.get("index")