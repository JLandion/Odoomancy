from odoo import models, fields


class OdoomancyCharacterFeat(models.Model):
    _name = "odoomancy.character.feat"
    _description = "Character Feat"

    character_id = fields.Many2one(
        "odoomancy.character",
        required=True,
        ondelete="cascade"
    )

    feat_id = fields.Many2one(
        "odoomancy.feat",
        required=True
    )

    acquired_level = fields.Integer()

    _sql_constraints = [
        (
            "character_feat_unique",
            "unique(character_id, feat_id)",
            "This feat is already assigned to the character."
        )
    ]
