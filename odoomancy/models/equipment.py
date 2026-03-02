from odoo import models, fields


class OdoomancyEquipmentCategory(models.Model):
    _name = "odoomancy.equipment.category"
    _description = "Equipment Category"
    _order = "name"

    name = fields.Char(required=True)
    index = fields.Char(required=True, index=True)


class OdoomancyWeaponProperty(models.Model):
    _name = "odoomancy.weapon.property"
    _description = "Weapon Property"
    _order = "name"

    name = fields.Char(required=True)
    index = fields.Char(required=True, index=True)


class OdoomancyEquipment(models.Model):
    _name = "odoomancy.equipment"
    _description = "Equipment"
    _order = "name"

    name = fields.Char(required=True)
    index = fields.Char(required=True, index=True)

    equipment_category_id = fields.Many2one(
        "odoomancy.equipment.category",
        required=True
    )

    cost_quantity = fields.Integer()
    cost_unit = fields.Char()

    weight = fields.Float()

    description = fields.Text()

    weapon_range = fields.Selection([
        ('melee', 'Melee'),
        ('ranged', 'Ranged')
    ])

    damage_dice = fields.Char()
    damage_type_id = fields.Many2one(
        "odoomancy.damage.type"
    )

    weapon_property_ids = fields.Many2many(
        "odoomancy.weapon.property",
        string="Weapon Properties"
    )

    armor_category = fields.Selection([
        ('light', 'Light'),
        ('medium', 'Medium'),
        ('heavy', 'Heavy'),
        ('shield', 'Shield')
    ])

    armor_class_base = fields.Integer()
    armor_dex_bonus = fields.Boolean()
    armor_max_bonus = fields.Integer()


