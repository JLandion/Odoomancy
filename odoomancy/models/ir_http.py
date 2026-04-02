from odoo import models
from odoo.http import request

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def color_scheme(self):
        if request and request.session.uid:
            return request.env.user.color_scheme or 'light'
        return 'light'