# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': 0,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'author' : "Mohanad Error",
    'website': 'https://www.mohanaderror.com',
    'depends' : ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment.xml',
        'views/actions.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/appointment_view.xml',
        'views/patient_tag.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install' : False,
    'license': 'LGPL-3',
}
