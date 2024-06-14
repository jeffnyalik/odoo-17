from odoo import api, fields, models

class SalesInherited(models.Model):
    _inherit = "res.users"
    property_id = fields.One2many("estate.property",
                                  "seller",
                                  string="Properties"
                                  )