from odoo import fields, models


class EquipmentCategory(models.Model):
    _name = 'equipment.category'

    name = fields.Char(string='Name')
