from odoo import models, fields


class OdoomancySpell(models.Model):
    _name = "odoomancy.spell"
    _description = "Spell"

    name = fields.Char(required=True)

    level = fields.Integer(required=True)
    school = fields.Char()

    casting_time = fields.Char()
    spell_range = fields.Char()
    duration = fields.Char()

    ritual = fields.Boolean(default=False)
    concentration = fields.Boolean(default=False)

    description = fields.Html()

    class_ids = fields.Many2many(
        "odoomancy.class",
        "odoomancy_spell_class_rel",
        "spell_id",
        "class_id",
        string="Classes"
    )
