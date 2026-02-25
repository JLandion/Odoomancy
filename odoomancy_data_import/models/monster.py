from odoo import models, fields


class OdoomancyMonster(models.Model):
    _inherit = "odoomancy.monster"

    api_index = fields.Char()