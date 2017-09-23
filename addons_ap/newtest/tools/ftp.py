# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _, SUPERUSER_ID

class ani_ftp(models.Model):
    _name = 'ani.ftp'
    _description = 'Ftp service'

    user = fields.Char('User', size=16, required=True)
    passwd = fields.Char('Password', size=16, required=True)
    path = fields.Char('Home', size=128, required=True)