{
    'name': "omo_device",
    'version': '1.0',
    'depends': ['base', 'mail', 'uom', 'product', 'stock'],
    'summary': """
                All about OMO Devices """,
    'author': "OMO Systems",
    'category': 'omo systems',
    'description': """
        Basic module for configuration OMO devices
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_inherit.xml',
        'views/product_template_inherit.xml',
        'views/device_action.xml',
        'views/omo_device_type.xml',
        'views/device_menu.xml',
        'views/stock_production_lot_inherit.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
