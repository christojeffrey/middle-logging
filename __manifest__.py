# -*- coding: utf-8 -*-
{
    'name': "Middle Logging",
    'summary': 'Module Odoo untuk middle logging. diambil dari cats dari spek. not edited yet selain nama dan summary',
    'description': 'Module Odoo untuk menyimpan dan menampilkan data kucing yang ada pada WillyWangky’s Pet Shop.',
    'sequence': -100,
    'author': "Thomas The Tank Engine",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cats_menus.xml',
        'views/cats_trees.xml',
        'views/cats_forms.xml',
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
