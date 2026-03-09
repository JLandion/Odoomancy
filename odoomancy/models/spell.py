from odoo import models, fields


class OdoomancySpellSlot(models.Model):
    _name = "odoomancy.spell.slot"
    _description = "Spell Slot"
    _order = "level"

    name = fields.Char(required=True)
    level = fields.Integer(required=True)
    value = fields.Char(required=True)
    type = fields.Selection([
        ("damage", "Damage"),
        ("heal", "Heal"),
    ], required=True)

class OdoomancySpell(models.Model):
    _name = "odoomancy.spell"
    _description = "Spell"
    _order = "level, name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)

    level = fields.Integer()

    casting_time = fields.Char()
    spell_range = fields.Char()
    duration = fields.Char()

    ritual = fields.Boolean()
    concentration = fields.Boolean()

    magic_school_id = fields.Many2one("odoomancy.magic.school")

    description = fields.Text()
    higher_level_description = fields.Text()

    # component_ids = fields.Many2many("odoomancy.spell.component")
    verbal = fields.Boolean(string="Verbal (V)")
    somatic = fields.Boolean(string="Somatic (S)")
    material = fields.Boolean(string="Material (M)")
    material_component = fields.Char()

    attack_type = fields.Char()

    class_ids = fields.Many2many("odoomancy.class")

    damage_type_id = fields.Many2one("odoomancy.damage.type")

    dc_type = fields.Many2one("odoomancy.ability.score")

    dc_success = fields.Selection([
        ("none", "None"),
        ("half", "Half"),
        ("other", "Other"),
    ])

    damage_at_slot_ids = fields.Many2many(
        "odoomancy.spell.slot",
        relation="odoomancy_spell_damage_slot_rel",
        column1="spell_id",
        column2="slot_id",
        domain=[('type', '=', 'damage')]
    )

    heal_at_slot_ids = fields.Many2many(
        "odoomancy.spell.slot",
        relation="odoomancy_spell_heal_slot_rel",
        column1="spell_id",
        column2="slot_id",
        domain=[('type', '=', 'heal')]
    )

    range = fields.Text()