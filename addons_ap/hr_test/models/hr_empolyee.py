# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _, SUPERUSER_ID

class ZtkEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"

    zsinid = fields.Integer(string="Ztk Attendance ID", help = "ID used for Employee of ZTK Attendance", default = 65536)
    udi = fields.Datetime(string="Check Time")