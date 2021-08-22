from odoo import fields, models, api, exceptions
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "The properties in the estate application"

    type_id = fields.Many2one("estate.property.type", string="Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_avaliability = fields.Date(string="Available From", copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],)
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = 0
            if record.offer_ids:
                record.best_price = max(record.mapped('offer_ids.price'))
                # record.best_price = record.offer_ids[0].price
                # for offer in record.offer_ids:
                #     if record.best_price < offer.price:
                #         record.best_price = offer.price
    
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = None
            self.garden_orientation = None

    def sell_property(self):
        for record in self:
            if record.state == "canceled":
                raise exceptions.UserError("Property cannot be sold after cancelling")
            else:    
                record.state = "sold"
        return True

    def cancel_property(self):
        for record in self:
            if record.state == "sold":
                raise exceptions.UserError("Property cannot be canceled after it was sold")
            else:    
                record.state = "canceled"
        return True
    
    def set_selling_price_and_buyer(self, accepted_offer):
        for record in self:
            for offer in record.offer_ids:
                if offer == accepted_offer:
                    record.selling_price = offer.price
                    print(record.selling_price)
                    record.buyer_id = offer.partner_id
                else:
                    offer.status = "refused"
                    print(offer.status)
                
