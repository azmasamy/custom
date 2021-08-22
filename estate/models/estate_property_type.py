from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The property types in the estate application"

    name = fields.Char(required=True)