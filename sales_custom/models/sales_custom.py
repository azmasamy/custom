# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date

class InheritedModel(models.Model):
    _inherit = "res.partner"
    age = fields.Integer(compute="_compute_age")
    date_of_birth = fields.Date()

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()
        if self.date_of_birth:
            self.age = today.year - self.date_of_birth.year
        else:
            self.age = 0
