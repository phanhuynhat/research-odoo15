# -*- coding: utf-8 -*-
{
    'name': "class_managerment",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': 3,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'views/classinfor.xml',
    'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ], 
    #thuộc apps
    'application': True,
    'installable': True,
    'auto_install': False,
}
