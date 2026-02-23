from odoo import models, fields


class OdoomancyCharacterSpell(models.Model):
    _name = "odoomancy.character.spell"
    _description = "Character Spell"

    character_id = fields.Many2one(
        "odoomancy.character",
        required=True,
        ondelete="cascade"
    )

    spell_id = fields.Many2one(
        "odoomancy.spell",
        required=True
    )

    prepared = fields.Boolean(default=False)
    uses_remaining = fields.Integer()
