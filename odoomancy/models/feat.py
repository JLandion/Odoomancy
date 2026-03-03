from odoo import models, fields


class OdoomancyFeat(models.Model):
    _name = "odoomancy.feat"
    _description = "Feat"

    name = fields.Char(required=True)
    description = fields.Html()

    # TODO: replace text by ability_score and minimum score (see API)
    prerequisite_text = fields.Text()
