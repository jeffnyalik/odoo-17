from odoo import fields, models, Command


class EstateAccount(models.Model):
    _inherit = "estate.property"

    # Inherit the action sold method in estate property model
    def action_sold(self):
        res = super().action_sold()

        # Prepare the invoice line values
        invoice_line_vals = [
            Command.create({
                'name': self.name,  # Description of the property
                'quantity': 1,  # You can change the quantity if needed
                'invoice_date': self.date_availability,
                'price_unit': self.expected_price,  # Use the selling price of the property
            })
        ]

        # prepare the invoice values
        invoice_vals = {
            'partner_id': self.buyer.id,  # Assuming the buyer is the customer
            'move_type': 'out_invoice',  # Customer Invoice
            'journal_id': self.env['account.journal'].search([('type', '=', 'sale')], limit=1).id,  # Sales Journal
            'invoice_line_ids': invoice_line_vals ## Include the invoice lines
        }

        #create the invoice
        self.env['account.move'].create(invoice_vals)
        print(res) ## debug the output
        return res

