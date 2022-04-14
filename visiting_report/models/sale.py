# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	visit_object = fields.Char(string="Visit Object")
	visit_start = fields.Datetime(string="Visit Start")
	visit_end = fields.Datetime(string="Visit End")
	visit_result = fields.Text(string="Visit Result")