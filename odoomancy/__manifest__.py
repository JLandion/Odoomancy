# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Odoomancy',
    'version': '0.0',
    'summary': 'Odoomancy for Odoomancers',
    'description': """
A different way to play D&D for and by Odoomancers
""",
    'data': ['security/ir.model.access.csv',
             'views/campaign_views.xml',
             'views/character_views.xml',
             'views/encounter_views.xml',
             'views/item_views.xml',
             'views/log_views.xml',
             'views/menu.xml',
             'views/monster_views.xml',
             'views/feat_views.xml',
             'views/spell_views.xml',],
    'installable': True,
    'application': True,
    'author': 'Perfidio',
    'license': 'LGPL-3',
}

