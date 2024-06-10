from odoo import api,fields,models

class TodoTask(models.Model):
    _inherit = ["todo.task"]
    _description = "Inherited module for todos"

    user_id = fields.Many2one("res.users", string="Responsible")
    date_deadline = fields.Date(string="Deadline")
