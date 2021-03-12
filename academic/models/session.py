from odoo import api, fields, models

class Course(models.Model):
    _name = 'academic.session'

    name = fields.Char("Nama", required=True, size=100)
    