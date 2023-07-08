# -*- coding: utf-8 -*-
{
    'name': "Partner",

    'summary': """
        My second task in odoo
        """,
    'description': """
        Long description of Partner's purpose
    """,

    'author': "Mohanad",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'sequence': 3,
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
