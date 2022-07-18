# -*- coding: utf-8 -*-
# ############################################################################################################
#                                   This addon was created by Muriel Rémi                                    #
#                                        Creation date: 03 August 2021                                       #
# ############################################################################################################
{
    'name' : "Mode de règlement",
    'version' : '1.1',
    'summary': "Mode de règlement",
    'sequence': -20,
    'author' : "VNTechnology",
    'description': """
       Mode de règlement
    """,
    'category': '',
    'website': 'https://vntechnology.eu',
    'images' : [],
    'depends' : ['base', 'sale'],
    'data': [
        "security/ir.model.access.csv",
        "views/payment_mode.xml",
        "views/partner.xml",
        "views/sale.xml",
        # "reports/bde_report_header.xml",
        # "reports/bde_report.xml",
        # "reports/report.xml",
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    # 'application': True,
    'auto_install': False,
}
