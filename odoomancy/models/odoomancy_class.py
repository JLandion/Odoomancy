from odoo import models, fields


class OdoomancyClass(models.Model):
    _name = "odoomancy.class"
    _description = "Class"

    name = fields.Char(required=True)
    description = fields.Text()

    spell_ids = fields.Many2many(
        "odoomancy.spell",
        "odoomancy_spell_class_rel",
        "class_id",
        "spell_id",
        string="Available Spells"
    )
