# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Animation Mrp",
    "version": "0.5",
    "author": "S.Jun",
    "category": "Manufacturing",
    "website": "http://www.oodo.com",
    # 'images': ['static/img/product_4-image.png'],
     "depends" : ["base","hr"],
    'data': [
        'views/env_view.xml',
        'views/category_view.xml',
        'views/stage_view.xml'
    ],
    "summary" : 'Tasks',
    'sequence': '1',
    # "init_xml" : [],
    "demo": [
        'demo/env_demo.xml',
        'demo/category_demo.xml'
    ],
    # "update_xml" : [],
    'application': True,
    "installable": True,
    # "active": False
    'auto_install': False,
    'qweb': [],
}