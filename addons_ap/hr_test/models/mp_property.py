# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, exceptions, _, SUPERUSER_ID

# 种类
class mp_type(models.Model):
    _name = "mp.type"
    _description = "Type"

    type_ids = fields.Integer(string="ID")
    name = fields.Char(string="Type")
    parent_id = fields.Many2one('mp.type', string="Parent")

# 资产
class property(models.Model):
    _name = "mp.property"
    _description = "Property"

    # 资产编号
    sid = fields.Char(string="Asset Number", required=True)
    # 名字
    name = fields.Char(string="Name", required=True)
    # 规格
    specifications = fields.Char(string="Specifications")
    # 型号
    model = fields.Char(string="Model")
    # 类别
    type_id = fields.Many2one('mp.type', string='Type', required=False)
    # 购买日期
    purchase = fields.Date(string="Purchase Date", default=fields.Date.today)
    # 单价
    price = fields.Float(string="Price", digits=(12,2))
    # 生产日期
    manufacture = fields.Date(string="Manufacture Date")
    # 编号
    sn = fields.Char(string="Serial number")
    # 用户
    user = fields.Many2one('hr.employee', string='Employee', required=False)
    #  配件-多个
    parts_list_ids = fields.One2many('mp.parts', 'pid', string='Parts')
    # 状态:在用/闲置/维修/报废
    status = fields.Selection([('idle', 'Idle'),
                               ('used', 'Used'),
                               ('repair', 'Repair'),
                               ('scrap', 'Scrap')],
                              string='Status',
                              default='idle')

# 配件
class parts(models.Model):
    _name = "mp.parts"
    _description = "Parts"

    pid = fields.Integer(string="id")
    name = fields.Char(string="Name")
    sn = fields.Char(string="Serial number")
    status = fields.Selection([('idle', 'Idle'),
                               ('used', 'Used'),
                               ('repair', 'Repair'),
                               ('scrap', 'Scrap')],
                              string='Status',
                              default='idle')

# 位置
class position(models.Model):
    _name = "mp.position"
    _description = "Storage location"

    poid = fields.Integer(string="id")
    position = fields.Char(string="Storage location")