# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	order_of_month = fields.Boolean(string="Order of Month", compute="_get_month", store=True)

	@api.depends('date_order')
	def _get_month(self):
		for record in self:
			record.order_of_month = record.date_order.month == fields.date.today().month

	@api.model
	def create(self, vals):
		res =  super(SaleOrder, self).create(vals)

		self.env['dashboard.parameter'].update_dashboard()

		return res

	def write(self, vals):
		res =  super(SaleOrder, self).write(vals)

		self.env['dashboard.parameter'].update_dashboard()

		return res