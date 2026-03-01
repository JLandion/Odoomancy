from odoo import fields, models
class CharacterEquipment(models.Model):
    _name = 'odoomancy.character.equipment'
    _description = 'Character Inventory'

    character_id = fields.Many2one(
        'odoomancy.character',
        required=True,
        ondelete='cascade'
    )

    equipment_id = fields.Many2one(
        'odoomancy.equipment',
        required=True
    )

    quantity = fields.Integer(default=1)