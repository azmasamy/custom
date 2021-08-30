from odoo import fields, models


class CustomerCategories(models.Model):
    _name = "customer.categories"
    _description = "The product categories history of the customer"

    customer_ids = fields.Many2many("res.partner")
    category_ids = fields.Many2many("product.category")

    quantity = fields.Integer()