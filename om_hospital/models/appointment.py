from odoo import api, fields, models

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string='Appointment Time' , default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    gender=fields.Selection(string="Gender", related="patient_id.gender")
    ref=fields.Char(string="Reference")
    doctor_id= fields.Many2one('res.users', string='Doctor')

    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([('0','Normal'),('1','Low'),('2','High'),('3','Very High'),('4','Very High1'),('5','Very High2')],string="Priority")
    state = fields.Selection(
        [('nhap', 'Nhap'), ('dang xac thuc', 'Dang xac thuc'), ('xac nhan', 'Xac nhan'),  ('huy', 'Huy')],
        string="Status", default='nhap')

    pharmacy_lines = fields.One2many('appointment.pharmacy.lines' ,'appointment_id',string='Pharmacy Lines')
    hide_sale_price = fields.Boolean(string='Hide Sales Price')

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


    def action_xac_thuc(self):
        for rec in self:
            rec.state= 'dang xac thuc'

    def action_xac_nhan(self):
        for rec in self:
            rec.state='xac nhan'

    def action_huy(self):
        for rec in self:
            rec.state='huy'


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(related="product_id.list_price")
    qty = fields.Integer(string='Quantity', default='1')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')






























