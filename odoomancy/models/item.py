from odoo import models, fields

class Item(models.Model):
    _name = 'odoomancy.item'
    _description = 'Item'
    name = fields.Char(required=True)
    description = fields.Text()

    item_type = fields.Selection([
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('consumable', 'Consumable'),
        ('misc', 'Miscellaneous')
    ], default='misc')
