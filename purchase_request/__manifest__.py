# -*- coding: utf-8 -*-
{
    'name': "Purchase YDS",
    'summary': """YDS task""",
    'description': """The module will provide functionality for requesting purchase orders and approving them before purchase orders are created""",
    'author': "Mohannad Mohammed",
    'website': "mohanad.salah404@gmail.com",
    'category': 'Purchase',
    'version': '0.1',
    'sequence': 4,
    'depends': ['base', 'purchase', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_request_views.xml',
        'views/purchase_request_lines_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
