from odoo import models, fields

class Equipment(models.Model):
    _name = 'odoomancy.equipment'
    _description = 'Equipment'
    name = fields.Char(required=True)
    description = fields.Text()

    equipment_type = fields.Selection([
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('consumable', 'Consumable'),
        ('misc', 'Miscellaneous')
    ], default='misc')
