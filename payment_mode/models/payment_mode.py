# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
from odoo.exceptions import UserError

class PaymentMode(models.Model):
    _name = 'payment.mode'
    _description = "Mode de règlement"

    name = fields.Char(string='Nom')
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Description sur la facture')
