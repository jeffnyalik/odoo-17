from odoo import api, models, fields
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
    property_type_id = fields.Many2one("estate.property.type", ondelete=None)
    tags_id = fields.Many2many("estate.property.tag", string="Tags")
    buyer = fields.Many2one("res.partner", string="Customer", copy=False)
    seller = fields.Many2one("res.users", string="Salesman",
                             default=lambda self:self.env.user,
                             index=True)
    # active = fields.Boolean(string="Active", default=True)

    class EstatePropertyType(models.Model):
        _name = "estate.property.type"
        _description = "Estate property type"

        name = fields.Char(string="Type", required=True)

    class EstatePropertyTag(models.Model):
        _name = "estate.property.tag"
        _description = "Property tags model"

        name = fields.Char(string="Tag", required=True)

    class EstatePropertyOffer(models.Model):
        _name = "estate.property.offer"
        _description = "Property offer model"
        price = fields.Float("Price", required=False)
        partner_id = fields.Many2one("res.partner", required=True)
        property_id = fields.Many2one("estate.property", required=True)
        status = fields.Selection([("accepted", "Accepted"), ("refused", "Refused")], copy=False)


