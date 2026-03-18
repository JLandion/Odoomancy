from odoo import models, fields


class OdoomancyClass(models.Model):
    _name = "odoomancy.class"
    _description = "Class"

    api_index = fields.Char()
    name = fields.Char(required=True)
    description = fields.Text()
    type = fields.Selection([
        ("barbarian", "Barbarian"), ("bard", "Bard"),
        ("cleric", "Cleric"), ("druid", "Druid"),
        ("fighter", "Fighter"), ("monk", "Monk"),
        ("paladin", "Paladin"), ("ranger", "Ranger"),
        ("rogue", "Rogue"), ("sorcerer", "Sorcerer"),
        ("warlock", "Warlock"), ("wizard", "Wizard")
    ], required=True)

    hit_die = fields.Integer(string="Hit Die", required=True)

    proficiencie_ids = fields.Many2many(
        "odoomancy.proficience",
        "class_proficience_rel",
        "class_id",
        "proficience_id",
        string="Proficiencies"
    )
    proficience_choice_ids = fields.Many2many(
        "odoomancy.proficience",
        "class_proficience_choice_rel",
        "class_id",
        "proficience_id",
        string="Proficiencies"
    )

    ability_scores = fields.Many2many(
        "odoomancy.ability.scores",
        "class_ability_scores_rel",
        "class_id",
        "ability_scores",
        string="Saving Throws (Ability Scores)"
    )

    equipment_starting = fields.Many2many("odoomancy.equipment",
                                          "class_equipment_starting_rel",
                                          "class_id",
                                          "equipment_id",
                                          string="Starting Equipment")

    equipment_options = fields.Many2many("odoomancy.equipment",
                                         "class_equipment_option_rel",
                                         "class_id",
                                         "equipment_option_id",
                                         string="Equipment Options")

    class_level_ids = fields.One2many("odoomancy.class.level",
                                      "class_id",
                                      string="Class Levels")

    spell_ids = fields.Many2many(
        "odoomancy.spell",
        "odoomancy_spell_class_rel",
        "class_id",
        "spell_id",
        string="Available Spells"
    )
