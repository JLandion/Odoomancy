from odoo import models
from ...services.dnd_api_service import DndApiService


class OdoomancyClassLevelImporter(models.TransientModel):
    _name = "odoomancy.class.level.importer"
    _inherit = "odoomancy.importer.mixin"

    _description = "Imports class levels of each class."

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.class.level"

    def _get_api_list(self, api):
        return [{"index":key} for key, _ in self.env['odoomancy.class']._fields['type'].selection]

    def _get_api_detail(self, api, ref):
        res = []
        levels = api.list_(f'classes/{ref}/levels')
        for level in levels:
            res.append({**level, "index": ref, })
        return res

    def _map_api_to_vals(self, _data):
        res = []
        for data in _data:
            level = data.get("level")
            api_index = data.get('index') + " - " + str(level)
            ability_score_bonuses = data.get("ability_score_bonuses")
            prof_bonus = data.get("prof_bonus")
            # features = data.get("features")
            class_specific = data.get("class_specific")
            class_ = None
            if "class" in data and "index" in data.get("skills"):
                class_ = data.get("skills").get("index")
                class_ = self.env['odoomancy.skills'].search([('name', '=', class_)], limit=1).id

            res.append({
                'api_index': api_index,
                'level': level,
                'ability_score_bonuses': ability_score_bonuses,
                'class_id': class_.id if len(class_) > 0 else None,
                'prof_bonus': prof_bonus,
                # 'features': features,
                'class_specific': class_specific,
            })
        return res

    def _get_external_key(self, ref, data):
        return ref.get('index')