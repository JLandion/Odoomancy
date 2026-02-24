from odoo import models, fields


class OdoomancyMonster(models.Model):
    _inherit = "odoomancy.monster"
    _description = "Monsters"

    api_index = fields.Char()