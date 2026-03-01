from odoo import models, fields, api
class Character(models.Model):
    _name = 'odoomancy.character'
    _description = 'Character'
    name = fields.Char(required=True)

    campaign_id = fields.Many2one(
        'odoomancy.campaign',
        required=True,
        ondelete='cascade'
    )

    player_id = fields.Many2one(
        'res.users',
        string='Player',
        required=True
    )

    character_class = fields.Char()
    level = fields.Integer(default=1)

    hp_current = fields.Integer(string="Current HP")
    hp_max = fields.Integer(string="Max. HP")

    state = fields.Selection([
        ('active', 'Active'),
        ('dead', 'Dead'),
        ('retired', 'Retired')
    ], default='active')

    strength = fields.Integer(default=10)
    dexterity = fields.Integer(default=10)
    constitution = fields.Integer(default=10)
    intelligence = fields.Integer(default=10)
    wisdom = fields.Integer(default=10)
    charisma = fields.Integer(default=10)

    equipment_ids = fields.One2many(
        'odoomancy.character.equipment',
        'character_id',
        string='Inventory'
    )

    class_id = fields.Many2one("odoomancy.class")
    race_id = fields.Many2one("odoomancy.race")

    spell_line_ids = fields.One2many(
        "odoomancy.character.spell",
        "character_id",
        string="Spells"
    )

    feat_line_ids = fields.One2many(
        "odoomancy.character.feat",
        "character_id",
        string="Feats"
    )


