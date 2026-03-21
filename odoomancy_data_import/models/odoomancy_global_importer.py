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
    ], string="Import", required=True)
