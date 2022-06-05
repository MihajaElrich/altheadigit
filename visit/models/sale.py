# -*- coding : utf-8 -*-
from odoo import api, models, fields

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	visit = fields.Many2one('visit', string="Visit")