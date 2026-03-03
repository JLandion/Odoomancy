from odoo import fields, models
class OdoomancyCampaignLog(models.Model):
    _name = 'odoomancy.campaign.log'
    _description = 'Campaign Log'

    name = fields.Char(required=True)

    campaign_id = fields.Many2one(
        'odoomancy.campaign',
        required=True,
        ondelete='cascade'
    )

    author_id = fields.Many2one(
        'res.users',
        default=lambda self: self.env.user
    )

    entry_date = fields.Datetime(default=fields.Datetime.now)

    content = fields.Html()

    visibility = fields.Selection([
        ('dm', 'DM'),
        ('all', 'All')
    ], default='all')
