from odoo import fields, models


class InheritedProductTemplate(models.Model):
    _inherit = "product.template"
    _name = "product.template"

    quantity_sold = fields.Integer(default=0, readonly=True)

    def update_quantity_sold(self, sold_quantity):
        self.quantity_sold += sold_quantity

    # def get_best_sellers(self, records_limit, category):
    #     if category == 'best_selling':
    #         return set(self.search(args=[], limit=records_limit, order='quantity_sold'))
    #     else:
    #         return set(self.search(args=[('categ_id', '=', category.id)], limit=records_limit, order='quantity_sold'))

    def get_unique_best_sellers(self, records_limit, category, previous_recommendations):
        recommended_products_ids = []
        for recommendation in previous_recommendations:
            recommended_products_ids.append(recommendation.id)
        if category == 'best_selling':
            return set(self.search(args=[('id', 'not in', recommended_products_ids)], limit=records_limit, order='quantity_sold desc'))
        else:
            return set(self.search(args=[('categ_id', '=', category.id), ('id', 'not in', recommended_products_ids)], limit=records_limit, order='quantity_sold desc'))
