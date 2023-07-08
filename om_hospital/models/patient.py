from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Hospital Patient'
    _rec_name = "name"
    
    

    name = fields.Char(string='Name', required=True, tracking= True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', tracking= True,  compute="_compute_age", readonly=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ], required= True, default= 'other', tracking= True)
    note = fields.Text(string='Description', tracking= True)
    image= fields.Image(string="Image")
    ref= fields.Char(string="Reference")
    active = fields.Boolean(string="Active", default=True)
    tag_ids = fields.Many2many('patient.tag',string="Tags")
    
    
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        
        for rec in self:
            today= date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age= 0
        