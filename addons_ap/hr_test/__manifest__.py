# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    # 模块名
    'name': 'ZKT_Attendances',
    # 分类
    'category': 'Human Resources',
    # 总述
    'summary': 'ZKT_attendances module',
    # 排序
    'sequence': 1,
    # 模块资料网站
    'website': 'https://www.tedo.com',
    # 作者
    'author':'Sunj',
    # 版本
    'version': '1.3',
    # 说明
    'description': """
This module aims to manage employee's attendances.
==================================================

Keeps account of the attendances of the employees on the basis of the
actions(Check in/Check out) performed by them.
       """,
    # 'images': [
    #     'images/hr_department.jpeg',
    #     'images/hr_employee.jpeg',
    #     'images/hr_job_position.jpeg',
    #     'static/src/img/default_image.png',
    # ],
    # 依赖模块（模块的目录名）

    'depends': ['hr'],
    # 必须安装的模块
    'data': [
        'views/property_view.xml',
        'data/property_defule.xml'
    ],
    # 测试数据(在勾选后加载)
    'demo': [
        'tests/property_demo.xml'
    ],
    # 是否可以安装
    'installable': True,
    # 是否是应用
    'application': True,
    # 是否是在支依赖模块安装后，自动安装
    'auto_install': False,
    'qweb': [],
}