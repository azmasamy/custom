from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
import datetime


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "The property offers in the estate application"

    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    price = fields.Float()
    status = fields.Selection(
        selection=[("accepted", "Accepted"), ("refused", "Refused")], copy=False
    )
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_compute_validity")

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = datetime.datetime.now() + relativedelta(days=record.validity)

    def _compute_validity(self):
        for record in self:
            my_time = datetime.datetime.now().time()
            my_datetime = datetime.datetime.combine(record.date_deadline, my_time)
            if record.create_date:
                delta = my_datetime - record.create_date
            else:
                delta = my_datetime - datetime.datetime.now()
            record.validity = delta.days

    
    def accept_offer(self):
        for record in self:
                record.status = "accepted"
                # self.env['estate.property'].set_selling_price_and_buyer(record)
        return True

    def refuse_offer(self):
        for record in self:
                record.status = "refused"
                # self.env['estate.property'].set_selling_price_and_buyer(record)
        return True

    
    
