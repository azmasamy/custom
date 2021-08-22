from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "The property tags in the estate application"

    name = fields.Char(required=True)