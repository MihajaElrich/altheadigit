# -*- coding: utf-8 -*-
{
    'name': "customer_website",

    'summary': """

       """,

    'description': """
       
    """,

    'author': "VNT",
    'website': "https://vntechnology.eu",
    'sequence' : 4,
    'license' : 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/partner.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
