from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Management model"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    is_child = fields.Boolean(string="Is child?", default=False)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([("male", "Male"),
                               ("female", "Female"),
                               ("others", "Others")],
                               string="Gender"
                              )
