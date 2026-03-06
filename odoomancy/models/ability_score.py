from odoo import fields, models


class OdoomancyAbilityScore(models.Model):
    _name = "odoomancy.ability.score"
    _description = "Ability Score"
    _order = "name"

    name = fields.Char(required=True)
    api_index = fields.Char(index=True)
    code = fields.Char(required=True)





