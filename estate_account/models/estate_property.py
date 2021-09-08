from odoo import models, exceptions


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sell_property(self):
        invoice_vals = self._prepare_invoice()
        self.env['account.move'].create(invoice_vals)
        return super().sell_property()

    def _prepare_invoice(self):
        self.ensure_one()
        journal = self.env['account.move'].with_context(
            default_move_type='out_invoice')._get_default_journal()
        if not journal:
            raise exceptions.UserError(_('Please define an accounting sales journal for the company %s (%s).') % (
                self.company_id.name, self.company_id.id))

        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id,
            'journal_id': journal.id,
            "invoice_line_ids": [
                (
                    0,
                    0,
                    {
                        "name": "Service fee",
                        "quantity": 1,
                        "price_unit": .06 * self.selling_price,
                    }
                ),
                (
                    0,
                    0,
                    {
                        "name": "administrative fees",
                        "quantity": 1,
                        "price_unit": 100,
                    },
                )
            ],
        }
        return invoice_vals
