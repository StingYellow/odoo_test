from odoo import api, fields, models
from odoo.fields import Many2many


class CancelAppointment(models.TransientModel):
    _name="cancel.appointment"
    _description = "Cancel Appointment"

    appointment_id = fields.Many2one('hospital.appointment',string='Appointment')