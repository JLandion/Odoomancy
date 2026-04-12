from odoo import models, fields


class OdoomancyTraits(models.Model):
    _name = "odoomancy.traits"
    _description = "Traits"

    name = fields.Char(required=True)
    api_index = fields.Char()
    races = fields.Many2many('odoomancy.race', string='Races')
    proficiencies = fields.Many2many('odoomancy.proficience', string='Proficiencies')
    description = fields.Text()
