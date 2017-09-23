# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _, SUPERUSER_ID

class status(models.Model):
  _name = 'ani.status'
  _description = 'Animation project for status'

  status_id = fields.Integer('ID of status', required=True)
  name = fields.Char('Status', size=64, required=True)

class ani_env_stage(models.Model):
    _name='ani.env.stage'
    _description = 'env of stage'

    sequence = fields.Integer("Sequence")
    envlstage = fields.Many2one('ani.env', 'Env ID', ondelete='cascade', select=True)
    stagelenv = fields.Many2one('ani.stage', 'Stage Name', ondelete='no action', select=True)
    parent = fields.Char('Parent', size=64)

    _order = 'sequence'

class ani_env(models.Model):
  _name = 'ani.env'
  _description = 'Animation of Project'

  env_id = fields.Char('NO.', size=64, required=True)
  name = fields.Char('Project Name', size=128, required=True)
  shortening = fields.Char('Shortening', size=4)
  parent = fields.Char('Parent', size=64)
  start_date = fields.Date('Start date')
  end_date = fields.Date('End date')
  days = fields.Integer('Days')
  priority = fields.Selection([(0,'Very important'),(2,'Important'),(5,'Medium'),(8,'Low'),(10,'Very Low')],string='Priority')
  status = fields.Selection([('draft','draft'),('wait_prove','waiting'),('proved','proved'),('rejected','reject')], string='Status', readonly=True, required=True)
  # user_id = fields.Many2one('res.users', 'Owner', help="Owner of the note stage.", required=True, ondelete='cascade')
  type_id = fields.Many2one('ani.category','Category', ondelete='no action', select=True)
  envlstage_id = fields.One2many('ani.env.stage', 'envlstage', 'Stage')

  _order = 'name'
  _defaults = {
    'status': lambda *a: 'draft',
    'priority': lambda *a: 5,
    'days': lambda *a: 0
    }

class ani_link(models.Model):
  _name = 'ani.link'
  _description = 'Link of Animation Process'

  link_id = fields.Integer('Link ID')
  number = fields.Integer('Number of Link',required=True)
  name = fields.Char('Name of link', size=128, required=True)
  process_id = fields.Char('Process ID', size=10)
  process_link_id = fields.Integer('Process Link ID')