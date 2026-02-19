from odoo import models, fields


class OdoomancyEncounter(models.Model):
    _name = "odoomancy.encounter"
    _description = "Campaign Encounter"

    name = fields.Char(required=True)

    campaign_id = fields.Many2one(
        "odoomancy.campaign",
        required=True,
        ondelete="cascade"
    )

    state = fields.Selection([
        ("planned", "Planned"),
        ("active", "Active"),
        ("finished", "Finished")
    ], default="planned")

    description = fields.Html()

    monster_line_ids = fields.One2many(
        "odoomancy.encounter.monster",
        "encounter_id",
        string="Monsters"
    )
