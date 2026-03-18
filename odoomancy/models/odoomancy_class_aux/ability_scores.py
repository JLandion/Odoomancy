from odoo import models, fields

class OdoomancyAbilityScores(models.Model):
    _name = "odoomancy.ability.scores"
    _description = "Odoomancy Ability Scores"

    name = fields.Selection([
        ("str", "STR"), ("dex", "DEX"),
        ("con", "CON"), ("int", "INT"),
        ("wis", "WIS"), ("cha", "CHA"),
    ], required=True)
    description = fields.Text(string = "Description", required=True)
    skill_id = fields.One2many(
        "odoomancy.skill",
        "ability_score_ids",
        string="Skills"
    )
    class_ids = fields.Many2many("odoomancy.class", string="Classes")