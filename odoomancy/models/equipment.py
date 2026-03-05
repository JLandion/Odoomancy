from odoo import models, fields


class OdoomancyWeaponProperty(models.Model):
    _name = "odoomancy.weapon.property"
    _description = "Weapon Property"
    _order = "name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)


class OdoomancyEquipment(models.Model):
    _name = "odoomancy.equipment"
    _description = "Equipment"
    _order = "name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)

    equipment_category_id = fields.Many2one(
        "odoomancy.equipment.category",
        required=True
    )

    equipment_type = fields.Selection([
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('gear', 'Adventuring Gear'),
        ('tool', 'Tool'),
        ('mount', 'Mount'),
    ])

    description = fields.Text()

    cost_quantity = fields.Float()
    cost_unit = fields.Selection([
        ('cp', 'Copper'),
        ('sp', 'Silver'),
        ('ep', 'Electrum'),
        ('gp', 'Gold'),
        ('pp', 'Platinum'),
    ])

    weight = fields.Float()

    range_normal = fields.Integer()
    range_long = fields.Integer()

    damage_dice = fields.Char()
    damage_type_id = fields.Many2one(
        "odoomancy.damage.type"
    )

    # TOOLS
    tool_category = fields.Selection([
        ('artisans-tools', "Artisan's Tools"),
        ('gaming-sets', "Gaming Sets"),
        ('musical-instruments', "Musical Instruments"),
        ('other-tools', "Other Tools"),
    ])

    # WEAPONS
    weapon_category = fields.Selection([
        ('simple', 'Simple'),
        ('martial', 'Martial'),
    ])
    weapon_range = fields.Selection([
        ('melee', 'Melee'),
        ('ranged', 'Ranged')
    ])
    weapon_property_ids = fields.Many2many(
        "odoomancy.weapon.property",
        string="Weapon Properties"
    )

    # ARMORS
    armor_category = fields.Selection([
        ('light', 'Light'),
        ('medium', 'Medium'),
        ('heavy', 'Heavy'),
        ('shield', 'Shield')
    ])
    armor_str_minimum = fields.Integer()
    armor_class_base = fields.Integer()
    armor_dex_bonus = fields.Boolean()
    armor_max_bonus = fields.Integer()