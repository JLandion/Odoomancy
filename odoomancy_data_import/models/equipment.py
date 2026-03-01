from odoo import models, fields


class OdoomancyEquipment(models.Model):
    _inherit = "odoomancy.equipment"

    api_index = fields.Char()