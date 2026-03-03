from odoo import models, fields, api

class OdoomancyCampaign(models.Model):
    _name = 'odoomancy.campaign'
    _description = 'Campaign'

    name = fields.Char(required=True)
    description = fields.Text(required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Done')
    ], default='draft', required=True)

    dm_id = fields.Many2one(
        'res.users',
        string='Dungeon Master',
        required=True
    )

    player_ids = fields.Many2many(
        'res.users',
        string='Players'
    )

    character_ids = fields.One2many(
        'odoomancy.character',
        'campaign_id',
        string='Characters'
    )
    log_ids = fields.One2many('odoomancy.campaign.log', 'campaign_id', string='Logs')

    start_date = fields.Date()
    end_date = fields.Date()