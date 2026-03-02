from odoo import models, fields


class OdoomancyMonster(models.Model):
    _name = "odoomancy.monster"
    _description = "Monsters"

    api_index = fields.Char()
    name = fields.Char(required=True)

    challenge_rating = fields.Float(string="CR")
    monster_type = fields.Char()
    size = fields.Char()
    alignment = fields.Char()

    hit_points = fields.Integer(string="Hit points")
    armor_class = fields.Integer()

    speed = fields.Char()
    type = fields.Char()
    strength = fields.Integer(default=10)
    dexterity = fields.Integer(default=10)
    constitution = fields.Integer(default=10)
    intelligence = fields.Integer(default=10)
    wisdom = fields.Integer(default=10)
    charisma = fields.Integer(default=10)
    spell_ids = fields.Many2many(
        "odoomancy.spell",
        "odoomancy_spell_monster_rel",
        "class_id",
        "spell_id",
        string="Available Spells"
    )

    description = fields.Html()
