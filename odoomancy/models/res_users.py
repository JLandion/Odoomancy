from odoo import models, fields
from odoo.http import request

class ResUsers(models.Model):
    _inherit = 'res.users'

    color_scheme = fields.Selection([
        ('default', 'Odoo Default'),
        ('light', 'Light'),
        ('dark', 'Dark'),
    ], string="Theme", default='light')

    def write(self, vals):
        result = super().write(vals)
        if 'color_scheme' in vals and request:
            request.future_response.set_cookie(
                'color_scheme',
                vals['color_scheme'],
                max_age=365 * 24 * 60 * 60
            )
        return result