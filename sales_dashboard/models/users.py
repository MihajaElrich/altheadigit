# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import date

class ResUsers(models.Model):
	_inherit = 'res.users'

	customer_count = fields.Integer(string="Customer Count", compute="_count_customer", store=True)

	def _count_customer(self):
		for record in self:
			sales = self.env['sale.order'].search([('user_id', '=', record.id)])

			customers = [sale.partner_id for sale in sales]

			customers = list(dict.fromkeys(customers))

			record.customer_count = len(customers)