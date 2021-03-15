from odoo import api, fields, models
import time

class Session(models.Model):
    _name = 'academic.session'

    # def search_date(self:
    #     return time.strftime("%Y-%m-%d"))

    name = fields.Char("Nama", required=True, size=100)
    
    course_id = fields.Many2one(comodel_name='academic.course', string='Course')
    
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')
    
    # start_date = fields.Date(string='Start Date', default=search_date)
    start_date = fields.Date(string='Start Date', default=lambda self: time.strftime("%Y-%m-%d"))
    
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

    image_small = fields.Binary(string='Image')
    
    
    
    # Function
    def _compute_taken_seats(self):
        for x in self:
            if x.seats > 0:
                x.taken_seats = 100.0 * len(x.attendee_ids) / x.seats
            else:
                x.taken_seats = 0.0
    
    # Onchange
    @api.onchange('seats')
    def ochange_seats(self):
        if self.seats > 0:
                self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
        else:
            self.taken_seats = 0.0
    
    @api.multi
    def _cek_instructor(self):
        for session in self:
            # session.instructor_id ada di dalam session.attendee_ids: partner_id
            # cara 1
            # x = []

            # for attendee in session.attendee_ids:
            #     x.append(attendee.partner_id.id)

            # x = [1,2,3,4]


            # cara 2
            # Baca dari Kanan
            x = [attendee.partner_id.id for attendee in session.attendee_ids]


            if session.instructor_id.id in x:
                return False
        
        return True

    # Constraint (Validasi)
    _constraints = [(_cek_instructor, 
        'Instruktur tidak boleh merangkap jadi Attendee', 
        ['instructor_id','attendee_ids'])]

    @api.multi
    def copy(self,default=None):
        #inherit duplicate (modif field name)
        default = dict(default or {}, name=self.name + " copy")
        # print "******"
        # print default
        # print "******"
        return super(Session, self).copy(default=default)