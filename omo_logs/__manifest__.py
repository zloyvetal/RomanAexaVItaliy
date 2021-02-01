# -*- coding: utf-8 -*-
# (C) 2021 OMO Systems (<"https://omo.systems/>)

{
    'name': "Omo Logs",
    'summary':  """
        Модуль для журналирования IoT устройств.
        Для более детальной информации посетите сайт.
    """,
    'description': """
        Модуль для ведения журналов и учета событий IoT устройств.
    """,
    'author': "OMO Systems",
    'website': "https://omo.systems/",
    'category': 'IoT',
    'version': '1.0',
    'depends': ['base', 'omo_device'],

    'data': [
        "security/ir.model.access.csv",
        "views/omo_logs_tree_view.xml",
        "views/omo_logs_form_view.xml",
        "views/omo_logs_action_view.xml",
        'views/stock_production_lot_inherit.xml',
        "views/menuitem.xml",

    ],


    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

