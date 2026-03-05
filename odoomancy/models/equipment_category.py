from odoo import models, fields


class OdoomancyEquipmentCategory(models.Model):
    _name = "odoomancy.equipment.category"
    _description = "Equipment Category"
    _order = "name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)