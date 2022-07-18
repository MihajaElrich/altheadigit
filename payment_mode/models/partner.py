# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerPaymentMode(models.Model):
    _inherit = 'res.partner'

    payment_mode_id = fields.Many2one('payment.mode', 'Mode de règlement')

