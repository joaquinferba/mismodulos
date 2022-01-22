# -*- coding: utf-8 -*-
{
    'name': "Mi revista",

    'summary': """
        Mi tercer módulo""",

    'description': """
        Si esto funciona hemos empezado bien
    """,

    'author': "Joaquín Fernández Baño",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','milibro2'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
               'views/mirevista_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
  #  'application': True,
}
