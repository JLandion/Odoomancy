from odoo import models
from ..services.dnd_api_service import DndApiService


class OdoomancySpellsImporter(models.TransientModel):
    _name = "odoomancy.spells.importer"
    _inherit = "odoomancy.importer.mixin"

    def _get_api_service(self):
        return DndApiService()

    def _get_model_name(self):
        return "odoomancy.spell"

    def _get_api_list(self, api):
        return api.list_spells().get("results", [])

    def _get_api_detail(self, api, ref):
        return api.get_spell(ref)

    def _map_api_to_vals(self, data):
        name = data.get("name")
        level = data.get("spell_level") or data.get("level")
        casting_time = data.get("casting_time")
        spell_range = data.get("range")
        duration = data.get("duration")
        ritual = data.get("ritual", False)
        concentration = data.get("concentration", False)

        # Description and higher level (arrays to HTML)
        desc = data.get("desc") or data.get("description") or []
        description = "<br/>".join(desc) if isinstance(desc, list) else desc or ""

        higher = data.get("higher_level") or []
        higher_level_description = "<br/>".join(higher) if isinstance(higher, list) else higher or ""

        # School (object with name)
        school = data.get("school")
        if isinstance(school, dict):
            school = school.get("name")

        # Components
        components = data.get("components", [])
        verbal = "V" in components if isinstance(components, list) else False
        somatic = "S" in components if isinstance(components, list) else False
        material = "M" in components if isinstance(components, list) else False
        material_component = data.get("material") or ""

        # Area of Effect
        aoe = data.get("area_of_effect") or {}
        area_of_effect_size = aoe.get("size") if isinstance(aoe, dict) else None
        area_of_effect_type = aoe.get("type") if isinstance(aoe, dict) else None

        # Attack type
        attack_type = data.get("attack_type")

        # Damage type
        # damage_type_id = None
        # damage_info = data.get("damage")
        # if damage_info and isinstance(damage_info, dict):
        #     damage_type = damage_info.get("damage_type")
        #     if damage_type and isinstance(damage_type, dict):
        #         damage_type_name = damage_type.get("name")
        #         damage_type_index = damage_type.get("index")
        #         if damage_type_name:
        #             damage_type_rec = self.env['odoomancy.damage.type'].search([('name', '=', damage_type_name)], limit=1)
        #             if not damage_type_rec:
        #                 damage_type_rec = self.env['odoomancy.damage.type'].create([{
        #                     'name': damage_type_name,
        #                     'api_index': damage_type_index
        #                 }])
        #             damage_type_id = damage_type_rec.id

        # Classes
        # class_ids = []
        # classes_data = data.get("classes", [])
        # for cls in classes_data:
        #     cls_name = cls.get("name")
        #     if cls_name:
        #         class_rec = self.env['odoomancy.class'].search([('name', '=', cls_name)], limit=1)
        #         if not class_rec:
        #             class_rec = self.env['odoomancy.class'].create([{'name': cls_name}])
        #         class_ids.append(class_rec.id)

        # Subclasses
        # subclass_ids = []
        # subclasses_data = data.get("subclasses", [])
        # for sub in subclasses_data:
        #     sub_name = sub.get("name")

        return {
            "api_index": data.get("index"),
            "name": name,
            # "magic_school_id": school,
            "level": level,
            "casting_time": casting_time,
            "spell_range": spell_range,
            "duration": duration,
            "ritual": ritual,
            "concentration": concentration,
            "description": description,
            "higher_level_description": higher_level_description,
            "verbal": verbal,
            "somatic": somatic,
            "material": material,
            "material_component": material_component,
            #"area_of_effect_size": area_of_effect_size,
            #"area_of_effect_type": area_of_effect_type,
            "attack_type": attack_type,
            # "damage_type_id": damage_type_id if damage_type_id else None,
            # "class_ids": [(6, 0, class_ids)],
            # "subclass_ids": [(6, 0, subclass_ids)],
        }

    def _get_external_key(self, ref, data):
        return data.get("index")