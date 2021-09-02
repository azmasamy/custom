from odoo import fields, models, api

class InheritedSalesOrder(models.Model):
    _inherit = "sale.order"
    _name = "sale.order"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res:
            for line in res.order_line:
                if line:
                    line.product_template_id.update_quantity_sold(
                        line.product_uom_qty)
                if res.partner_id:
                    res.partner_id.customer_category_ids.update_customer_categories(
                        res.partner_id, line.product_template_id.categ_id, line.product_uom_qty)
        return res