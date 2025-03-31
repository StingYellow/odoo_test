from odoo import api, fields, models

class PatientTag(models.Model):
    _name="patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string='Name' , require=True)
    active = fields.Boolean(string="Active" ,default =True)
