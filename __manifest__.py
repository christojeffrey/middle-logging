# -*- coding: utf-8 -*-
{
    'name': "Middle Logging",
    'summary': 'Module Odoo untuk middle logging.',
    'description': 'Module Odoo untuk menyimpan dan menampilkan data middle logging yang ada pada PT Berkah Sempurna Prima.',
    'sequence': -100,
    'author': "SI Berkahnya Sempurna",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/middle_logging_menus.xml',
        'views/middle_logging_trees.xml',
        'views/middle_logging_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
