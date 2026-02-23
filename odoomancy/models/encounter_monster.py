from odoo import models, fields


class OdoomancyEncounterMonster(models.Model):
    _name = "odoomancy.encounter.monster"
    _description = "Encounter Monster Instance"

    encounter_id = fields.Many2one(
        "odoomancy.encounter",
        required=True,
        ondelete="cascade"
    )

    monster_id = fields.Many2one(
        "odoomancy.monster",
        required=True
    )

    quantity = fields.Integer(default=1)

    hp_current = fields.Integer()
    initiative = fields.Integer()
