# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import date

class ResUsers(models.Model):
	_inherit = 'res.users'

	customer_count = fields.Integer(string="Customer Count", compute="_count_customer", store=True)
	clients = fields.Many2many('res.partner', string='Clients', compute="_count_customer", group_operator="count_distinct")

	def _count_customer(self):
		for record in self:
			sales = self.env['sale.order'].search([('user_id', '=', record.id)])

			customers = [sale.partner_id for sale in sales]

			customers = list(dict.fromkeys(customers))

			record.clients = self.env['res.partner'].browse([customer.id for customer in customers])

			record.customer_count = len(customers)

			raise UserError("clients : %s\ncustomer_count: %s" % (record.clients, record.customer_count))