from openerp.osv import osv, fields

class ani_stage(osv.osv):
    _name = 'ani.stage'
    _description = 'Stage of Animation'
    _columns = {
      'stage_id': fields.one2many('ani.env.stage', 'stagelenv', 'Stage ID'),
      'sequence': fields.integer('Sequence', required=True),
      'name': fields.char('Stage Name',size=128,required=True),
      'shoting': fields.char('Shoting',size=2,required=True),
      'folds': fields.char('Folds',size=32,required=True)
    }
    _order = 'sequence,name'
ani_stage()

class ani_stage_list(osv.osv):
    _name = 'ani.stage.list'
    _description = 'The file list of Stage'
    _columns = {
        'file_list_id': fields.integer('List ID',required=True),
        'name': fields.char('List Name',size=128,required=True),
        'formate': fields.char('File Formate',size=128,required=True),
        'must': fields.boolean('Must'),
        'chack': fields.boolean('Chack')
    }
    _order = 'sequence'
    _defaults = {
        'must': lambda *a: 0,
        'chack': lambda *a: 0
    }

class ani_format(osv.osv):
    _name = 'ani.format'
    _description = 'The file use formate'
    _columns = {
        'name': fields.char('Formate',size=128, required=True),
        'note': fields.char('Note',size=256)
    }