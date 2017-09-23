# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields

class status(osv.osv):
  _name = 'ani.status'
  _description = 'Animation project for status'
  _columns = {
    'status_id': fields.integer('ID of status',required= True),
    'name':fields.char('Status', size=64 , required=True),
  }


class ani_env_stage(osv.osv):
    _name='ani.env.stage'
    _description = 'env of stage'
    _columns = {
        'sequence': fields.integer("Sequence"),
        'envlstage': fields.many2one('ani.env', 'Env ID', ondelete='cascade', select=True),
        'stagelenv': fields.many2one('ani.stage','Stage Name', ondelete='no action', select=True),
        'parent': fields.char('Parent', size=64)
    }
    _order = 'sequence'

class ani_env(osv.osv):
  _name = 'ani.env'
  _description = 'Animation of Project'

  _columns = {
    'env_id': fields.char('NO.', size=64, required=True),
    'name': fields.char('Project Name', size=128, required=True),
    'shortening': fields.char('Shortening', size=4),
    'parent': fields.char('Parent', size=64),
    'start_date': fields.date('Start date'),
    'end_date': fields.date('End date'),
    'days': fields.integer('Days'),
    'priority': fields.selection([(0,'Very important'),(2,'Important'),(5,'Medium'),(8,'Low'),(10,'Very Low')],string='Priority', required=True),
    'status': fields.selection([('draft','draft'),('wait_prove','waiting'),('proved','proved'),('rejected','reject')], string='Status', readonly=True, required=True),
#    'user_id': fields.many2one('res.users', 'Owner', help="Owner of the note stage.", required=True, ondelete='cascade'),
    'type_id': fields.many2one('ani.category','Category', ondelete='no action', select=True),
    'envlstage_id':fields.one2many('ani.env.stage', 'envlstage', 'Stage')
    }
  _order = 'name'
  _defaults = {
    'status': lambda *a: 'draft',
    'priority': lambda *a: 5,
    'days': lambda *a: 0
    }

class ani_link(osv.osv):
  _name = 'ani.link'
  _description = 'Link of Animation Process'
  _columns = {
    'link_id': fields.integer('Link ID'),
    'number':fields.integer('Number of Link',required=True),
    'name': fields.char('Name of link', size=128, required=True),
    'process_id': fields.char('Process ID', size=10),
    'process_link_id':fields.integer('Process Link ID')
  }
