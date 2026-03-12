from odoo import models, fields

class OdoomancyProficience(models.Model):
    _name = "odoomancy.proficience"
    _description = "Use in Classes"

    name = fields.Char(required=True)
