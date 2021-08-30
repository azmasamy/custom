from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "The property tags in the estate application"
    _order = "name"
    _sql_constraints = [
        ('unique_tage_name', 'UNIQUE (name)', 'There is already a tag with the same name')
    ]


    name = fields.Char(required=True)
    color = fields.Integer('Color')

    