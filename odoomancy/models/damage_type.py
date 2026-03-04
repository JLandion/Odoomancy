from odoo import models, fields

class OdoomancyDamageType(models.Model):
    _name = "odoomancy.damage.type"
    _description = "Damage Type"
    _order = "name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)

