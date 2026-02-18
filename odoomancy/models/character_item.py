from odoo import fields, models
class CharacterItem(models.Model):
    _name = 'odoomancy.character.item'
    _description = 'Character Inventory'

    character_id = fields.Many2one(
        'odoomancy.character',
        required=True,
        ondelete='cascade'
    )

    item_id = fields.Many2one(
        'odoomancy.item',
        required=True
    )

    quantity = fields.Integer(default=1)