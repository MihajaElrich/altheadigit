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

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('visit')
		return super(Visit, self).create(vals)