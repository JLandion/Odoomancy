from odoo import models, fields

class OdoomancyFeatures(models.Model):
    _name = "odoomancy.features"
    _description = "Use in Classes"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True)
    class_id = fields.Many2one(comodel_name='odoomancy.class', required=True)
    level = fields.Integer(string="Level", required=True)
    prerequisites = fields.Json(string="Prerequisites")
    description = fields.Text(string="Description")
    expertise_options = fields.Many2many('odoomancy.proficience', string="Expertise (features)")
    choose_expertise_options = fields.Integer(string="Choose Expertise Options")
    invocations = fields.Json(string="Invocations")
