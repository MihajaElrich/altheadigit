# -*- coding : utf-8 -*-
from odoo import api, models, fields, _

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	bl_import = fields.Boolean(string="BL Import", default=True)
	inv_import = fields.Boolean(string="Invoice Import")