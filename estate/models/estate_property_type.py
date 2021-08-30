from odoo import fields, models, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The property types in the estate application"
    _order = "sequence"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property', "type_id", string="Properties")
    sequence = fields.Integer('Sequence', default=1, help="Used to order property types.")
    offer_ids = fields.One2many('estate.property.offer', "property_type_id", string="Offers")
    offer_count = fields.Integer(compute="_compute_offers_count")

    @api.depends("offer_ids")
    def _compute_offers_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
    