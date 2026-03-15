from odoo import models, fields


class OdoomancyClassLevel(models.Model):
    _name = "odoomancy.class.level"
    _description = "Class Level"

    api_index = fields.Char(string="Api Index")
    class_id = fields.Many2one("odoomancy.class", required=True, ondelete="cascade")
    level = fields.Integer(required=True)
    prof_bonus = fields.Integer(string="Profile Bonus")
    features = fields.Text(string="Level Features") # TODO: hacer modelo
    ability_score_bonuses = fields.Integer(string="Ability Score Bonuses")
    class_specific = fields.Json(string="Class Specific skill upgrades")
