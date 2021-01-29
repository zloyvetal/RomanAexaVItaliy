# -*- coding: utf-8 -*-
# (C) 2020 OMO Systems (<"https://omo.systems/>)
{
    "name": "OMO Users",
    "summary": "Module create a model of omo_user",
    "version": " 14.0.1",
    "category": "Uncategorized",
    'author': "OMO Systems",
    'website': "https://omo.systems/",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        'base',
        'omo_device',
        'stock',
    ],
    "data": [
        'views/res_partner_inherit.xml',
        'views/res_users_inherit.xml',
        'views/res_company_inherit.xml',
        'security/ir.model.access.csv',
    ],
    "demo": [
    ],
    "qweb": [
    ],
    "application": True,
    "installable": True,
    'auto_install': False,
}
