# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class SaleOrderPaymentMode(models.Model):
    _inherit = 'sale.order'

    payment_mode_id = fields.Many2one('payment.mode', 'Mode de règlement')

    @api.onchange('partner_id')
    def _change_partner_id(self):
        if self.partner_id.payment_mode_id :
            self.payment_mode_id = self.partner_id.payment_mode_id