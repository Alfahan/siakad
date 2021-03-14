from odoo import api, fields, models

class Attendee(models.Model):
    _name = "academic.attendee"

    name = fields.Char("Register Number", required=True, size=100)

    session_id = fields.Many2one(
        comodel_name='academic.session', 
        string='Session')
    
    partner_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Partner')
    
        
    # Constraint Sql
    _sql_constraints = [
        ('sql_cek_name','UNIQUE(name)','No Regist same as other'),
        ('sql_cek_attendee','UNIQUE(session_id, partner_id)','this person is already registered')
    ]