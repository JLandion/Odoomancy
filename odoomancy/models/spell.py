from odoo import models, fields


class OdoomancyMagicSchool(models.Model):
    _name = "odoomancy.magic.school"
    _description = "Magic School"
    _order = "name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)


class OdoomancySpellComponent(models.Model):
    _name = "odoomancy.spell.component"
    _description = "Spell Component"
    _order = "name"

    name = fields.Char(required=True)
    code = fields.Char(required=True)



class OdoomancySpellDamage(models.Model):
    _name = "odoomancy.spell.damage"
    _description = "Spell Damage"

    spell_id = fields.Many2one(
        "odoomancy.spell",
        required=True,
        ondelete="cascade"
    )

    scaling_type = fields.Selection([
        ("slot_level", "Spell Slot Level"),
        ("character_level", "Character Level"),
    ], required=True)

    level = fields.Integer(required=True)

    damage = fields.Char(required=True)


class OdoomancySpell(models.Model):
    _name = "odoomancy.spell"
    _description = "Spell"
    _order = "level, name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)

    level = fields.Integer()
    magic_school_id = fields.Many2one("odoomancy.magic.school")

    casting_time = fields.Char()
    spell_range = fields.Char()
    duration = fields.Char()

    concentration = fields.Boolean()
    ritual = fields.Boolean()

    description = fields.Text()
    higher_level_description = fields.Text()

    material = fields.Char()

    component_ids = fields.Many2many("odoomancy.spell.component")

    class_ids = fields.Many2many("odoomancy.class")

    damage_type_id = fields.Many2one("odoomancy.damage.type")

    dc_type = fields.Many2one("odoomancy.ability.score")

    dc_success = fields.Selection([
        ("none", "None"),
        ("half", "Half"),
        ("other", "Other"),
    ])

    range = fields.Text()

    damage_line_ids = fields.One2many(
        "odoomancy.spell.damage",
        "spell_id"
    )

