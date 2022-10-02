# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'SO Delivery Charges',
    'version' : '1.2',
    'summary': 'Delivery Charges',
    'sequence': 10,
    'description': """
    Includes delivery charge for SO and virtually included in sale order line and virtually included in invoice
    """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : ['sale', 'account'],
    'data': [
        'views/delivery_charge.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web._assets_primary_variables': [
        ],
        'web.assets_backend': [

        ],
        'web.assets_frontend': [
        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
        ],
    },
    'license': 'LGPL-3',
}
