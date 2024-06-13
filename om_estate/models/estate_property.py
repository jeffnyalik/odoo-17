from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, timedelta
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    # define the model fields
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postal Code")
    date_availability = fields.Date(
        string="Availability Date",
        default=lambda self: (
            datetime.now() + timedelta(days=90)
        ).strftime("%Y-%m-%d")
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Number of Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage?", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        string="Type",
        selection=[("north", "North"), ("east", "East"), ("west", "West")],
        help="This field is to show case north, east and west directions"
    )
    state = fields.Selection(
        string="Status",
        selection=[("new", "New"),
                   ("offer received", "Offer Received"),
                   ("offer accepted", "Offer Accepted"),
                   ("sold", "Sold"),
                   ("canceled", "Canceled"),
                   ],
        required=True,
        copy=False,
        default="new"
    )
    property_type_id = fields.Many2one("estate.property.type",ondelete=None)
    tags_id = fields.Many2many("estate.property.tag", string="Tags")
    buyer = fields.Many2one("res.partner", string="Customer", copy=False)
    type_ids = fields.Many2one("estate.property.type", string="Property types")
    seller = fields.Many2one("res.users", string="Salesman",
                             default=lambda self:self.env.user,
                             index=True)
    offer_ids = fields.One2many("estate.property.offer",
                                "property_id",
                                string="Property offers")
    total_area = fields.Float(string="Total Area", compute="_computeTotal")
    best_price = fields.Float(string="Best Offer", compute="_compute_best_price", store=True)
    validity = fields.Integer("Validity period", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")


    def action_cancel(self):
        for rec in self:
            if rec.state:
                rec.state = "canceled"
        return True

    def action_sold(self):
        for rec in self:
            if rec.state == "canceled":
                raise UserError("A canceled property can not be sold")
            elif rec.state == "sold":
                rec.state = "sold"
                # raise UserError("Sold value has already been set")
            else:
                # Assign the value to sold
                rec.state == "sold"

        return True


    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for rec in self:
            if rec.create_date:
                rec.date_deadline = (rec.create_date + timedelta(days=rec.validity))
            else:
                rec.date_deadline = fields.Date.today() + timedelta(days=rec.validity)
        return

    def _inverse_date_deadline(self):
        for rec in self:
            if rec.create_date and rec.date_deadline:
                duration = (rec.date_deadline - rec.create_date.date()).days
                rec.validity = duration
            else:
                rec.validity = 7
        return

    # Onchange garden area and orientation
    @api.onchange("garden_area", "garden_orientation")
    def _onchange_area_orientation(self):
        self.garden_area = 200
        self.garden_orientation = "north"

    # Compute the sum of the living area and garden area
    @api.depends("living_area", "garden_area")
    def _computeTotal(self):
        for rec in self:
            rec.total_area = (rec.living_area + rec.garden_area)
            return rec.total_area
        return True

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for rec in self:
            if rec.offer_ids:
                rec.best_price = max(rec.offer_ids.mapped('price'))
            else:
                rec.best_price = "0.0"
        return


    # active = fields.Boolean(string="Active", default=True)

    class EstatePropertyType(models.Model):
        _name = "estate.property.type"
        _description = "Estate property type"

        name = fields.Char(string="Type", required=True)
        property_ids = fields.One2many("estate.property","property_type_id")

        def get_offers(self):
            pass

        def offers_count(self):
            pass

    class EstatePropertyTag(models.Model):
        _name = "estate.property.tag"
        _description = "Property tags model"

        name = fields.Char(string="Tag", required=True)
        color = fields.Integer(string="Color")

    class EstatePropertyOffer(models.Model):
        _name = "estate.property.offer"
        _description = "Property offer model"
        price = fields.Float("Price", required=False)
        partner_id = fields.Many2one("res.partner", required=True)
        property_id = fields.Many2one("estate.property", required=True)
        status = fields.Selection([("new", "New"),
                                   ("accepted", "Accepted"),
                                   ("refused", "Refused")], default="new", copy=False)

        def action_accept(self):
            for rec in self:
                if rec.status == "accepted":
                    rec.status == "accepted"
                    rec.property_id.selling_price = rec.property_id.expected_price
            return True

        def action_refuse(self):
            for rec in self:
                if rec.status and rec.status == "refused":
                    rec.property_id.selling_price = 0.0
                    rec.property_id.expected_price = rec.property_id.expected_price
            return True




