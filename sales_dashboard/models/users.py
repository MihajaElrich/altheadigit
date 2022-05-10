# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime as dt
from calendar import monthrange

class ResUsers(models.Model):
	_inherit = 'res.users'

	monthly_amount = fields.Float(string="Monthly Amount", compute="_compute_amount", store=True)

	def _compute_amount(self):
		for record in self:
			month_sales = self.env['sale.order'].search(['&', 
				('user_id', '=', record.id), 
				('date_order', '>=', dt.strptime('01-%s-%s' % (dt.today().month, dt.today().year), '%d-%m-%Y')),
				('date_order', '<=', dt.strptime('%s-%s-%s 23:59:59' % (monthrange(dt.today().year, dt.today().month)[1], dt.today().month, dt.today().year), '%d-%m-%Y %H:%M:%S'))
			])

			# raise UserError(month_sales)
			record.monthly_amount = sum([sale.amount_total for sale in month_sales])