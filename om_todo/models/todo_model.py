from odoo import fields, models, api

class TodoTask(models.Model):
    _name = "todo.task"
    _description = "Todo task model"

    name = fields.Char(string="Description", required=True)
    is_done = fields.Boolean(string="Done", default=False)
    active = fields.Boolean(string="Active?", default=True)

    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    def toggle_active(self):
        if self.is_done:
            self.active = self.active
        return True

    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True



