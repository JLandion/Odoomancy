from odoo import models, fields

class OdoomancySkills(models.Model):
    _name = "odoomancy.skill"
    _description = "Skill"

    name = fields.Char(required=True)
    description = fields.Text()


class SavingThrows(models.Model):
    _name = "odoomancy.saving_throw"
    _description = "Saving Throw"

    full_name = fields.Char(required=True)
    type = fields.Selection([
        ("cha", "CHA"), ("con", "CON"),
        ("dex", "DEX"), ("int", "INT"),
        ("str", "STR"), ("wis", "WIS"),
    ], required=True)
    description = fields.Text()
    skills = fields.Many2many(
        "odoomancy.skill",
        "odoomancy_saving_throw_skill_rel",
        "saving_throw_id",
        "skill_id",
        string="Associated Skills"
    )