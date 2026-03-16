{
    "name": "Odoomancy Data Import",
    "summary": "Importing data from external APIs for Odoomancy",
    "description": """
    Integration module that allows you to import external data 
    from the public D&D 5e API into Odoomancy module models.
    """,
    "version": "19.0.1.0.0",
    "category": "Games",
    "author": "Odoomancers",
    "license": "LGPL-3",
    "depends": [
        "base",
        "odoomancy",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/global_import_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'odoomancy_data_import/static/src/js/import_progress.js',
        ],
    },
    "qweb": [],
    "installable": True,
    "application": False,
}