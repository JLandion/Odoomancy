from odoo import models, fields


class OdoomancyClassLevel(models.Model):
    _name = "odoomancy.class_level"
    _description = "Class Level"

    class_id = fields.Many2one("odoomancy.class", required=True, ondelete="cascade")
    level = fields.Integer(required=True)
    features = fields.Text(string="Level Features")
    ability_score_bonuses = fields.Text(string="Ability Score Bonuses")
    class_specific = fields.Json(string="Class Specific skill upgrades")