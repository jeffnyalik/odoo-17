from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order" #sale_order
    _description = "Inherited model"

    sale_descriptions = fields.Char(required=False, string="Sale Description")
    sale_number = fields.Integer(required=False, string="Sales number")

