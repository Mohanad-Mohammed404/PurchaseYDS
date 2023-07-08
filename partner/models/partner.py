from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(
        string="Is Student?",
        default=False,
        required=True
    )
    birth_date = fields.Date(
        string="Date of Birth",
        required=True
    )

    @api.constrains('birth_date')
    def _check_birth_date(self):
        for rec in self:
            if rec.birth_date > date.today():
                raise ValidationError("Birth date must be in the past!")
