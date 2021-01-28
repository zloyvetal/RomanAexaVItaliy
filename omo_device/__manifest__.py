{
    'name': "omo_device",
    'version': '1.0',
    'depends': ['base', 'mail', 'uom', 'product'],
    'summary': """
                This module create a library ticket""",
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
        'views/device_menu.xml',
        'views/omo_device_type.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
