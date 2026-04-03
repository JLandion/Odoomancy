from odoo import models, fields


class OdoomancyRace(models.Model):
    _name = "odoomancy.race"
    _description = "Race"

    name = fields.Char(required=True)
    description = fields.Text()

class OdoomancySubRace(models.Model):
    _name = "odoomancy.subrace"
    _description = "Race"

    name = fields.Char(required=True)
    description = fields.Text()