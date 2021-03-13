from odoo import api, fields, models

class Course(models.Model):
    _name = 'academic.session'

    name = fields.Char("Nama", required=True, size=100)
    
    course_id = fields.Many2one(comodel_name='academic.course', string='Course')
    
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')
    
    start_date = fields.Date(string='Start Date')
    
    duration = fields.Integer(string='Duration')
    
    seats = fields.Integer(string='Seats')
    
    active = fields.Boolean("Is Active", default=True)

    attendee_ids = fields.One2many(
        comodel_name='academic.attendee', 
        # FK 
        inverse_name='session_id', 
        string='Session')

    taken_seats = fields.Float(
        string='Taken Seats',
        compute='_compute_taken_seats')
    
    # Function
    def _compute_taken_seats(self):
        for x in self:
            x.taken_seats = 99.9
    
    
    
    