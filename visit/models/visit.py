# -*- coding : utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import UserError
from datetime import datetime as dt

class Visit(models.Model):
	_name = 'visit'
	_description = 'Visit'

	name = fields.Char(string="Number")
	customer = fields.Many2one('res.partner', string="Customer")
	obj = fields.Selection([
		('prospecting', _('Prospecting')),
		('courtesy', _('Courtesy Visit')),
		('order_taking', _('Order Taking')),
		('merchandising', _('Merchandising')),
		('recovery', _('Recovery')),
		('litigation', _('Litigation Management')),
		('promotion_proposal', _('Promotion Proposal'))
	],string="Object")
	start_datetime = fields.Datetime(string="Start Datetime")
	end_datetime = fields.Datetime(string="End Datetime")
	result = fields.Text(string="Result")

	customer_stocks = fields.One2many('customer.stock', 'visit', string="Customer Stocks", auto_join=True, copy=True)

	other_comments = fields.Text(string="Other Comments")

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('visit')
		return super(Visit, self).create(vals)

class CustomerStock(models.Model):
	_name = 'customer.stock'
	_description = 'Customer Stock'

	product = fields.Many2one('product.product', string="Product")
	customer = fields.Many2one('res.partner', string="Customer", compute="_get_customer")
	stock = fields.Float(string="Stock")

	visit = fields.Many2one('visit', string="Visit Reference", ondelete="cascade", readonly=True)

	@api.depends('visit.customer')
	def _get_customer(self):
		for record in self:
			record.customer = record.visit.customer