# -*- coding: utf-8 -*-

from odoo import models, fields, api


class customer_website(models.Model):
    _inherit = 'website'

    quotation_customer = fields.Many2many('res.partner', string="Clients", compute = '_compute_customers', store = False)

    def _compute_customers(self):
        for website in self:
            cust = self.env['res.partner'].search([('customer_rank', '>', 0)])
            website.quotation_customer = cust
    
class customer_on_quotation(models.Model) :
    _inherit = 'res.users'

    customer_in_quotation_id = fields.Integer(string="ID du Client en cours de saisie de devis")
    customer_in_quotation_name = fields.Char(string="Nom du Client en cours de saisie de devis")
    