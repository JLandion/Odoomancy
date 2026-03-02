from odoo import models, fields


class OdoomancyCharacterFeat(models.Model):
    _name = "odoomancy.character.feat"
    _description = "Character Feat"

    character_id = fields.Many2one(
        "odoomancy.character",
        required=True,
        ondelete="cascade"
    )

    feat_id = fields.Many2one(
        "odoomancy.feat",
        required=True
    )

    acquired_level = fields.Integer()


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


class OdoomancyCharacterSpell(models.Model):
    _name = "odoomancy.character.spell"
    _description = "Character Spell"

    character_id = fields.Many2one(
        "odoomancy.character",
        required=True,
        ondelete="cascade"
    )

    spell_id = fields.Many2one(
        "odoomancy.spell",
        required=True
    )

    prepared = fields.Boolean(default=False)
    uses_remaining = fields.Integer()


class OdoomancyCharacter(models.Model):
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


