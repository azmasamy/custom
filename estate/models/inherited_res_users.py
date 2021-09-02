from odoo import fields, models

class InheritedResUsers(models.Model):
    _inherit = "res.users"
    _name = "res.users"

    property_users_ids = fields.One2many( 'estate.property','salesperson_id', String='Properties',domain=[('state','in',('new', 'offer_received',))])
    # property_usr_ids = fields.Many2many( 'estate.property', String='Properties',domain="[('salesperson_id','=',id)]")