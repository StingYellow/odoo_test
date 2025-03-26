from odoo import api, fields, models

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string='Appointment Time' , default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    gender=fields.Selection(string="Gender", related="patient_id.gender")
    ref=fields.Char(string="Reference" , readonly=False)




    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref