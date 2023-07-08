from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Hospital Appointment'
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.patient', string="Patient Name")
    gender = fields.Selection(related="patient_id.gender")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(
        string="Booking Date",
        default=fields.Date.context_today,
        help="This is the booking Date")
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')],
        string="Status",
        default='draft',
        required=True
    )
    doctor_id = fields.Many2one('res.users', string="Doctor")
    pharmacy_id = fields.One2many('appointment.pharmacy','appointment_id', string="Pharmacy ID")
    hide_price = fields.Boolean(string="Hide Price")

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button clicked!!!!!!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'the code is executed in log',
                'type': 'rainbow_man',
            }
        }

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_cancel(self):
        action = self.env.ref('om_hospital.cancel_appointment_wizard_action').read()[0]
        return action


    def action_draft(self):
        for rec in self:
            rec.state = 'draft'


class AppointmentPharmacy(models.Model):
    _name='appointment.pharmacy'
    _description='Appointment Pharmacy'

    product_id= fields.Many2one('product.product')
    price_unit = fields.Float(related="product_id.list_price", string="Price")
    qty = fields.Integer(string="Quantity")
    appointment_id= fields.Many2one('hospital.appointment' , string="Appointment")