# -*- coding : utf-8 -*-
from odoo import api, models, fields
from odoo.exceptions import UserError
from datetime import datetime as dt

class Visit(models.Model):
	_name = 'visit'
	_description = 'Visit'

	name = fields.Char(string="Number")
	customer = fields.Many2one('res.partner', string="Customer")
	obj = fields.Char(string="Object")
	start_datetime = fields.Datetime(string="Start Datetime")
	end_datetime = fields.Datetime(string="End Datetime")
	result = fields.Text(string="Result")

	customer_stocks = fields.One2many('customer.stock', 'visit', string="Customer Stocks", auto_join=True, copy=True)

	competing_products = fields.Char(string="Competing Products")
	marketing_watch = fields.Char(string="Marketing Watch")

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