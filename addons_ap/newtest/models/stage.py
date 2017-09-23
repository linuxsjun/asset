# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _, SUPERUSER_ID

class ani_stage(models.Model):
    _name = 'ani.stage'
    _description = 'Stage of Animation'
    stage_id = fields.One2many('ani.env.stage', 'stagelenv', 'Stage ID')
    sequence = fields.Integer('Sequence', required=True)
    name = fields.Char('Stage Name', size=128, required=True)
    shoting = fields.Char('Shoting', size=2, required=True)
    folds = fields.Char('Folds', size=32, required=True)

    _order = 'sequence,name'

class ani_stage_list(models.Model):
    _name = 'ani.stage.list'
    _description = 'The file list of Stage'

    file_list_id = fields.Integer('List ID', required=True)
    name = fields.Char('List Name', size=128, required=True)
    formate = fields.Char('File Formate', size=128, required=True)
    must = fields.Boolean('Must')
    chack = fields.Boolean('Chack')

    _order = 'sequence'
    _defaults = {
        'must': lambda *a: 0,
        'chack': lambda *a: 0
    }
class ani_format(models.Model):
    _name = 'ani.format'
    _description = 'The file use formate'

    name = fields.Char('Formate', size=128, required=True)
    note = fields.Char('Note', size=256)