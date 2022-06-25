# -*- coding: utf-8 -*-
{
    'name': "website_sale_order_confirmation",

    'summary': """
        website sale order confirmation
            """,

    'license' : 'LGPL-3',

    'description': """
        website sale order confirmation
            """,

    'author': "VNT",
    'website': "https://vntechnology.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
