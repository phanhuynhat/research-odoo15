# -*- coding: utf-8 -*-
{
    'name': "New Page",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        WELCOME NEW PAGE 
    """,

    'author': "Nhat",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'license': 'LGPL-3',
    "sequence": '1',

    'data': [
        # 'security/ir.model.access.csv',
        'templates/web.xml',
        # 'views/views.xml',
        
    ],
    'assets': {
        # 'web.assets_qweb': [
        #     'new-page/static/src/**/*.xml',
        # ],
        'web._assets_primary_variables': [
            'new-page/static/src/colors.scss',
        ],
        # 'web._assets_backend_helpers': [
        #     'muk_web_theme/static/src/variables.scss',
        #     'muk_web_theme/static/src/mixins.scss',
        # ],
        # 'web.assets_backend': [
        #     'muk_web_theme/static/src/webclient/**/*.scss',
        #     'muk_web_theme/static/src/webclient/**/*.js',
        #     'muk_web_theme/static/src/search/**/*.scss',
        #     'muk_web_theme/static/src/search/**/*.js',
        #     'muk_web_theme/static/src/legacy/**/*.scss',
        #     'muk_web_theme/static/src/legacy/**/*.js',
        # ],
    },
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
}
