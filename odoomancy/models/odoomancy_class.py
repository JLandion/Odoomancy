from odoo import models, fields


class OdoomancyClass(models.Model):
    _name = "odoomancy.class"
    _description = "Class"

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

    proficience_description = fields.Text(string="Proficiencies Description")
    proficiencie_id = fields.Many2many(
        "odoomancy.proficience",
        "odoomancy_class_proficience_rel",
        "class_id",
        "proficience_id",
        string="Proficiencies"
    )
    proficience_choice_ids = fields.Many2many(
        "odoomancy.proficience",
        "odoomancy_class_proficience_choice_rel",
        "class_id",
        "proficience_id",
        string="Proficiencies"
    )

    saving_throws = fields.Many2many(
        "odoomancy.saving_throw",
        "odoomancy_class_saving_throw_rel",
        "class_id",
        "saving_throw_id",
        string="Saving Throws"
    )

    equipment_starting = fields.Many2many("odoomancy.equipment",
                                          "odoomancy_class_equipment_starting_rel",
                                          "class_id",
                                          "equipment_id",
                                          string="Starting Equipment")

    equipment_options = fields.Many2many("odoomancy.equipment",
                                         "odoomancy_class_equipment_option_rel",
                                         "class_id",
                                         "equipment_option_id",
                                         string="Equipment Options")

    class_level_ids = fields.One2many("odoomancy.class_level",
                                      "class_id",
                                      string="Class Levels")

    spell_ids = fields.Many2many(
        "odoomancy.spell",
        "odoomancy_spell_class_rel",
        "class_id",
        "spell_id",
        string="Available Spells"
    )


