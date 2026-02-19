from odoo import models, fields


class OdoomancyMonster(models.Model):
    _name = "odoomancy.monster"
    _description = "Monster"

    name = fields.Char(required=True)

    challenge_rating = fields.Float(string="CR")
    monster_type = fields.Char()
    size = fields.Char()
    alignment = fields.Char()

    hp_base = fields.Integer(string="Base HP")
    armor_class = fields.Integer()

    speed = fields.Char()

    strength = fields.Integer(default=10)
    dexterity = fields.Integer(default=10)
    constitution = fields.Integer(default=10)
    intelligence = fields.Integer(default=10)
    wisdom = fields.Integer(default=10)
    charisma = fields.Integer(default=10)

    description = fields.Html()
