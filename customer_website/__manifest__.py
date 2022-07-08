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
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account', 'website'],
    'data': [
        'views/templates.xml',
        'views/partner.xml'
    ],
    # 'assets' : {
    #     'web.assets_frontend' : [
    #         'customer_website/static/src/js/jquery3.6.0.min.js',
    #         'customer_website/static/src/css/select2.min.css',
    #         'customer_website/static/src/js/althea.js',
    #         'customer_website/static/src/js/select2.min.js',
    #     ],
    # },
}
