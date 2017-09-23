from openerp.osv import osv, fields

class ani_ftp(osv.osv):
    _name = 'ani.ftp'
    _description = 'Ftp service'
    _columns = {
      'user': fields.char('User',size=16,required=True),
      'passwd':fields.char('Password',size=16,required=True),
      'path': fields.char('Home',size=128,required=True)
      }