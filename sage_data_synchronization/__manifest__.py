# -*- coding: utf-8 -*-
{
    'name': "sage_data_synchronization",

    'summary': """
        Synchronisation des données articles et clients de sage vers odoo
        """,

    'description': """
        
    """,

    'author': "VNT",
    'website': "https://vntechnology.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/sync_data.xml',
        'data/sync_task.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
