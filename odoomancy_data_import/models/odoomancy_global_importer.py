from odoo import models, fields

class OdoomancyGlobalImporter(models.TransientModel):
    _name = "odoomancy.global.importer"
    _inherit = "odoomancy.importer.mixin"
    _description = "Global D&D Importer"

    importer_model = fields.Selection([
        ('odoomancy.class.importer', 'Classes'),
        ('odoomancy.class.level.importer', 'Class Levels'),
        ('odoomancy.monster.importer', 'Monsters'),
        ('odoomancy.spells.importer', 'Spells'),
    ], string="Import", required=True)
