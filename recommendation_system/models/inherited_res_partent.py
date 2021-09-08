from odoo import fields, models, api
import math


class InheritedResPartner(models.Model):
    _inherit = "res.partner"
    _name = "res.partner"

    customer_category_ids = fields.One2many(
        'customer.categories', 'customer_ids')
    recommendations = fields.Text(compute="_get_recommended_products")

    @api.depends("customer_category_ids")
    def _get_recommended_products(self):
        recommendation_count = 20
        self.recommendations = ""
        products_recommended = set()

        for customer in self:
            if customer.customer_category_ids:
                recommendations_count_per_category = self._calc_categories_percentages(
                    customer.customer_category_ids, recommendation_count)
                for category_recommendation in recommendations_count_per_category:
                    products_recommended.update(self.env['product.template'].get_unique_best_sellers(
                        category_recommendation['recommendations_count'], category_recommendation['category'], products_recommended))
            else:
                products_recommended = self.env['product.template'].get_unique_best_sellers(
                    recommendation_count, 'best_selling', products_recommended)

            products_recommended = list(products_recommended)
            products_recommended.sort(key=lambda x: x.quantity_sold, reverse=True)
            self.recommendations = self._get_recommended_products_string(
                products_recommended)

    def _calc_categories_percentages(self, customer_category_purchases, recommendations_requested):
        total_quantity_sold = 0
        total_recommendations_calculated = 0
        recommendation_count_per_category = []
        for category_purchase in customer_category_purchases:
            total_quantity_sold += category_purchase.quantity
        for category_purchase in customer_category_purchases:
            recommended_products_count = math.floor(v
                (category_purchase.quantity / total_quantity_sold) * 20)
            if recommended_products_count > math.floor(recommendations_requested / 2):
                recommended_products_count = math.floor(
                    recommendations_requested / 2)
            total_recommendations_calculated += recommended_products_count
            recommendation_count_per_category.append({
                'category': category_purchase.category_ids,
                'recommendations_count': recommended_products_count
            })
        if total_recommendations_calculated < recommendations_requested:
            recommendation_count_per_category.append({
                'category': 'best_selling',
                'recommendations_count': recommended_products_count
            })
        return recommendation_count_per_category

    def _get_recommended_products_string(self, products_recommended):
        recommendations_string = ""
        for product in products_recommended:
            recommendations_string += str(product.name) + \
                " - " + str(product.quantity_sold) + " - " + str(product.categ_id.name) + "\n"
        return recommendations_string
