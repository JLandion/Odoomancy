# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Odoomancy',
    'version': '19.0.1.0.0',
    'summary': 'Odoomancy for Odoomancers',
    'description': """
A different way to play D&D for and by Odoomancers
""",
    'depends':['base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/campaign_views.xml',
        'views/character_views.xml',
        'views/encounter_views.xml',
        'views/equipment_views.xml',
        'views/log_views.xml',
        'views/monster_views.xml',
        'views/feat_views.xml',
        'views/spell_views.xml',
        'views/class_views.xml',
        'views/class_aux_views.xml',
        'views/class_views.xml',
        'views/class_aux_views.xml',
        'views/menu.xml',
        'views/res_users_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'odoomancy/static/src/js/color_scheme.js',
            'odoomancy/static/src/scss/color_scheme.scss',
            'odoomancy/static/src/scss/dark-color-scheme.scss',
            'odoomancy/static/src/scss/light-color-scheme.scss',
        ],
    },
    'installable': True,
    'application': True,
    'author': 'Odoomancers',
    'license': 'LGPL-3',
}

