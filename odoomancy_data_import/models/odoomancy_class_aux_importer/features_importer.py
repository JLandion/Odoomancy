from odoo import models
from ...services.dnd_api_service import DndApiService


class OdoomancyFeaturesImporter(models.TransientModel):
    _name = "odoomancy.features.importer"
    _inherit = "odoomancy.importer.mixin"

    _description = "Imports features levels of each class."

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.features"

    def _get_api_list(self, api):
        return api.list_('features').get("results", [])

    def _get_api_detail(self, api, ref):
        return api.get_('features', ref)

    def _map_api_to_vals(self, data):
        name = data.get("name")
        api_index = data.get('index')

        desc = data.get("desc") or data.get("description") or []
        description = "<br/>".join(desc) if isinstance(desc, list) else desc or ""

        prerequisites = data.get("prerequisites") or []
        prerequisites = "<br/>".join(prerequisites) if prerequisites else ""

        level = data.get("level")
        class_ = None
        if "class" in data and "index" in data.get("class"):
            class_ = data.get("class").get("index")
            class_ = self.env['odoomancy.class'].search([('type', '=', class_)], limit=1).id

        expertise_options = None
        choose = None
        invocations = None
        if "feature_specific" in data and "expertise_options" in data.get("feature_specific"):
            fs = data.get("feature_specific").get("expertise_options")
            if "choose" in fs:
                choose = fs.get("choose")
            if "from" in fs and "options" in fs.get("from"):
                from_ = fs.get("from").get("options")
                for i in from_:
                    expertise_options = self.env['odoomancy.proficience'].search([('api-index', '=', i.get('index'))], limit=1)
        if "feature_specific" in data and "invocations" in data.get("feature_specific"):
            invocations = data.get("feature_specific").get("invocations")

        return{
            'name': name,
            'api_index': api_index,
            'class_id': class_,
            'level': level,
            'prerequisites': prerequisites,
            'description': description,
            'expertise_options': expertise_options,
            'choose_expertise_options': choose,
            'invocations': invocations
        }

    def _get_external_key(self, ref, data):
        return data.get("index")
