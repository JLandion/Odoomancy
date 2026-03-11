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

    def _selection_label_to_key(self, model, field_name, label):
        if not label:
            return False

        selection = dict(self.env[model]._fields[field_name].selection)
        reverse_selection = {v: k for k, v in selection.items()}

        return reverse_selection.get(label)

    def _equipment_selection(self, field_name, label):
        return self._selection_label_to_key("odoomancy.equipment", field_name, label)

    def _map_api_to_vals(self, data):
        name = data.get("name")
        api_index = data.get("index")

        # -------------------------
        # CATEGORY
        # -------------------------
        category = data.get("equipment_category")
        equipment_category_id = None

        if isinstance(category, dict):
            cat_name = category.get("name")
            cat_index = category.get("index")

            cat = self.env["odoomancy.equipment.category"].search(
                [("api_index", "=", cat_index)], limit=1
            )
            if not cat:
                cat = self.env["odoomancy.equipment.category"].create({
                    "name": cat_name,
                    "api_index": cat_index,
                })
            equipment_category_id = cat.id

        # -------------------------
        # DESCRIPTION
        # -------------------------
        desc = data.get("desc") or []
        description = "<br/>".join(desc) if isinstance(desc, list) else desc or ""

        # -------------------------
        # COST
        # -------------------------
        cost = data.get("cost") or {}
        cost_quantity = cost.get("quantity")
        cost_unit = cost.get("unit")

        # -------------------------
        # WEIGHT
        # -------------------------
        weight = data.get("weight")

        # -------------------------
        # RANGE
        # -------------------------
        range_data = data.get("range", {})
        range_normal = range_data.get("normal")
        range_long = range_data.get("long")


        # -------------------------
        # DAMAGE
        # -------------------------
        damage_dice = None
        damage_type_id = None

        damage = data.get("damage")
        if isinstance(damage, dict):
            damage_dice = damage.get("damage_dice")

            damage_type = damage.get("damage_type")
            if isinstance(damage_type, dict):
                dt_name = damage_type.get("name")
                dt_index = damage_type.get("index")

                dt = self.env["odoomancy.damage.type"].search(
                    [("api_index", "=", dt_index)], limit=1
                )
                if not dt:
                    dt = self.env["odoomancy.damage.type"].create({
                        "name": dt_name,
                        "api_index": dt_index,
                    })
                damage_type_id = dt.id

        # -------------------------
        # WEAPON INFO
        # -------------------------
        weapon_category = self._equipment_selection("weapon_category", data.get("weapon_category"))
        weapon_range = self._equipment_selection("weapon_range", data.get("weapon_range"))

        weapon_property_ids = []
        properties = data.get("properties", [])

        for prop in properties:
            prop_name = prop.get("name")
            prop_index = prop.get("index")

            rec = self.env["odoomancy.weapon.property"].search(
                [("api_index", "=", prop_index)], limit=1
            )
            if not rec:
                rec = self.env["odoomancy.weapon.property"].create({
                    "name": prop_name,
                    "api_index": prop_index,
                })

            weapon_property_ids.append(rec.id)

        # -------------------------
        # ARMOR INFO
        # -------------------------
        armor_category = self._equipment_selection("armor_category", data.get("armor_category"))

        armor_class = data.get("armor_class") or {}
        if "armor" in data.get("index"):
            print(data.get("index"))

        armor_class_base = armor_class.get("base")
        armor_dex_bonus = armor_class.get("dex_bonus")
        armor_max_bonus = armor_class.get("max_bonus")

        armor_str_minimum = data.get("str_minimum")

        # -------------------------
        # TOOL CATEGORY
        # -------------------------
        tool_category = self._equipment_selection("tool_category", data.get("tool_category"))

        # -------------------------
        # EQUIPMENT TYPE (derived)
        # -------------------------

        if weapon_category:
            equipment_type = "weapon"
        elif armor_category:
            equipment_type = "armor"
        elif tool_category:
            equipment_type = "tool"
        elif tool_category:
            equipment_type = "gear"
        else:
            equipment_type = None

        return {
            "api_index": api_index,
            "name": name,
            "equipment_category_id": equipment_category_id,
            "equipment_type": equipment_type,
            "description": description,
            "cost_quantity": cost_quantity,
            "cost_unit": cost_unit,
            "weight": weight,
            "range_normal": range_normal,
            "range_long": range_long,
            "damage_dice": damage_dice,
            "damage_type_id": damage_type_id,
            "weapon_category": weapon_category,
            "weapon_range": weapon_range,
            "weapon_property_ids": [(6, 0, weapon_property_ids)],
            "armor_category": armor_category,
            "armor_str_minimum": armor_str_minimum,
            "armor_class_base": armor_class_base,
            "armor_dex_bonus": armor_dex_bonus,
            "armor_max_bonus": armor_max_bonus,
            "tool_category": tool_category,
        }

    def _get_external_key(self, ref, data):
        return data.get("index")