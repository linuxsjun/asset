# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields

class ani_category(osv.osv):
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

    _name = 'ani.category'
    _description = 'category of Animation'
    _columns = {
        'category_id': fields.one2many('ani.env', 'type_id', 'Type ID'),
        'name': fields.char('Name', required=True),
        'complete_name': fields.function(_name_get_fnc, type="char", string='Name'),
        'parent_id': fields.many2one('ani.category', 'Parent Category',select=True, ondelete='cascade'),
        'child_id': fields.one2many('ani.category', 'parent_id', string='Child Categories'),
        'shortening': fields.char('Short', size=3),
        'show': fields.boolean('Show')
    }
    _order='parent_id'