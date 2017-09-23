# -*- encoding: utf-8 -*-
from odoo import models, fields, api, exceptions, _, SUPERUSER_ID

class ani_category(models.Model):
    '''
    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name','parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res

    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)
    '''

    _name = 'ani.category'
    _description = 'category of Animation'

    category_id = fields.One2many('ani.env', 'type_id', 'Type ID')
    name = fields.Char('Name', required=True)
    # complete_name' = fields.function(_name_get_fnc, type="char", string='Name')
    complete_name = fields.Char('Complete Name', size=32)
    parent_id = fields.Many2one('ani.category', 'Parent Category',select=True, ondelete='cascade')
    child_id = fields.One2many('ani.category', 'parent_id', string='Child Categories')
    shortening =fields.Char('Short', size=3)
    show = fields.Boolean('Show')

    _order = 'parent_id'