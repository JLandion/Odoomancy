from odoo import models, fields


class OdoomancySkill(models.Model):
    _name = 'odoomancy.skill'
    _description = 'Odoomancy Skill'

    name = fields.Selection([
        ("acrobatics", "Acrobatics"),
        ("animal-handling", "Animal Handling"),
        ("arcana", "Arcana"),
        ("athletics", "Athletics"),
        ("deception", "Deception"),
        ("history", "History"),
        ("insight", "Insight"),
        ("intimidation", "Intimidation"),
        ("investigation", "Investigation"),
        ("medicine", "Medicine"),
        ("nature", "Nature"),
        ("perception", "Perception"),
        ("performance", "Performance"),
        ("persuasion", "Persuasion"),
        ("religion", "Religion"),
        ("sleight-of-hand", "Sleight of Hand"),
        ("stealth", "Stealth"),
        ("survival", "Survival"),
    ], string="Skill")
    description = fields.Text(required=True)
    ability_score_ids = fields.Many2one("odoomancy.ability.scores", string="Ability Score")

