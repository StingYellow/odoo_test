from odoo import api, fields, models

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string='Appointment Time' , default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    gender=fields.Selection(string="Gender", related="patient_id.gender")
    ref=fields.Char(string="Reference")

    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([('0','Normal'),('1','Low'),('2','High'),('3','Very High'),('4','Very High1'),('5','Very High2')],string="Priority")
    state = fields.Selection(
        [('nhap', 'Nhap'), ('dang xac thuc', 'Dang xac thuc'), ('xac nhan', 'Xac nhan'),  ('huy', 'Huy')],
        string="Status", default='nhap')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_open_facebook(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.facebook.com/',
            'target': 'new',  # Mở trong tab mới
        }

    def action_test(self):
        return {
            'effect':{
                'fadeout':'slow',
                'message':'Thanh cong',
                'type': 'rainbow_man',

            }
        }