from odoo import fields, models, api


class CustomerCategories(models.Model):
    _name = "customer.categories"
    _description = "The product categories history of the customer"

    customer_ids = fields.Many2one("res.partner")
    category_ids = fields.Many2one("product.category")

    quantity = fields.Integer()

    def update_customer_categories(self, customer_id, category_id, product_quantity):
        if not self.search([('customer_ids', '=', customer_id.id), ('category_ids', '=', category_id.id)]):
            vals = {
                'customer_ids': customer_id.id,
                'category_ids': category_id.id,
                'quantity': product_quantity
            }
            self.create(vals)
