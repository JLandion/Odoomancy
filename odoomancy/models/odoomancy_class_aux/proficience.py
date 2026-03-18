from odoo import models, fields

class OdoomancyProficience(models.Model):
    _name = "odoomancy.proficience"
    _description = "Use in Classes"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True)
    type = fields.Char(required=True)
    class_id = fields.Many2many("odoomancy.class", string="Classes")
    # races = fields.Many2many("odoomancy.races", string="Races")
    skill = fields.Many2many("odoomancy.skill", string="Skills")
