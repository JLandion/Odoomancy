from odoo import models, fields

class OdoomancyGlobalImporter(models.TransientModel):
    _name = "odoomancy.global.importer"
    _inherit = "odoomancy.importer.mixin"
    _description = "Global D&D Importer"

    importer_model = fields.Selection([
        ('odoomancy.class.importer', 'Classes'),
        ('odoomancy.equipment.importer', 'Equipment'),
        ('odoomancy.class.level.importer', 'Class Levels'),
        ('odoomancy.monster.importer', 'Monsters'),
        ('odoomancy.spells.importer', 'Spells'),
        ('odoomancy.skills.importer', 'Skills'),
        ('odoomancy.ability.scores.importer', 'Ability Scores'),
        ('odoomancy.features.importer', 'Features'),
        ('odoomancy.proficience.importer', 'Proficiencies')
    ], string="Import", required=True)

    count_classes = fields.Integer("Classes", compute="compute_fields")
    count_equipments = fields.Integer("Equipments", compute="compute_fields")
    count_class_level = fields.Integer("Class Level", compute="compute_fields")
    count_monsters = fields.Integer("Monsters", compute="compute_fields")
    count_spells = fields.Integer("Spells", compute="compute_fields")
    count_skills = fields.Integer("Skills", compute="compute_fields")
    count_ability_scores = fields.Integer("Ability Scores", compute="compute_fields")
    count_features = fields.Integer("Features", compute="compute_fields")
    count_proficience = fields.Integer("Proficiencies", compute="compute_fields")
    # count_ = fields.Integer("", compute="compute_fields")

    def compute_fields(self):
        self.count_classes = self.env['odoomancy.class'].search_count([])
        self.count_equipments = self.env['odoomancy.equipment'].search_count([])
        self.count_class_level = self.env['odoomancy.class.level'].search_count([])
        self.count_monsters = self.env['odoomancy.monster'].search_count([])
        self.count_spells = self.env['odoomancy.spell'].search_count([])
        self.count_skills = self.env['odoomancy.skill'].search_count([])
        self.count_ability_scores = self.env['odoomancy.ability.scores'].search_count([])
        self.count_features = self.env['odoomancy.features'].search_count([])
        self.count_proficience = self.env['odoomancy.proficience'].search_count([])
        #self.count_ = self.env['odoomancy.'].search_count([])
