{
    "name": "Odoomancy Data Import",
    "summary": "Importing data from external APIs for Odoomancy",
    "description": """
    Integration module that allows you to import external data 
    from the public D&D 5e API into Odoomancy module models.
    """,
    "version": "19.0.1.0.0",
    "category": "Games",
    "author": "Perfidio",
    "license": "LGPL-3",
    "depends": [
        "base",
        "odoomancy",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/monster_import_views.xml',
        'views/spells_import_views.xml',
        'views/equipment_import_views.xml',
    ],
    "qweb": [],
    "installable": True,
    "application": False,
}