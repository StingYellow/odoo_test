from odoo import fields, models , api , _
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Hospital Patient'
    _rec_name = 'name'


    ref = fields.Char(string='Reference', required=True ,tracking=True)
    name = fields.Char(string="Hospital Name", required=True ,tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True, tracking=True)
    age = fields.Integer(string="Hospital Age", compute='_compute_age',required=True , tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", required=True ,tracking=True)

    active = fields.Boolean(string="Active", default=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = (today.year - rec.date_of_birth.year)
            else:
                rec.age = 0
