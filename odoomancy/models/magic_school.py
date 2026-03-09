from odoo import fields, models


class OdoomancyMagicSchool(models.Model):
    _name = "odoomancy.magic.school"
    _description = "Magic School"
    _order = "name"

    name = fields.Char(required=True)
    api_index = fields.Char(required=True, index=True)