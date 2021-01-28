# -*- coding: utf-8 -*-
# (C) 2020 OMO Systems (<"https://omo.systems/>)
{
    "name": "OMO Users",
    "summary": "Module for model omo_user",
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
        'views/omo_users_view.xml',
        'security/ir.model.access.csv',
    ],
    "demo": [
    ],
    "qweb": [
    ],
    "application": False,
    "installable": True,
    "autoinstall": False,
}
