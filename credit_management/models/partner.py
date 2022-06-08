# -*- encoding: utf-8 -*-

from odoo import fields, api, models

class ResPartner(models.Model):
	_inherit = 'res.partner'

	currency_id = fields.Many2one('res.currency', string="Currency", readonly=True)
	odoo_credit = fields.Monetary(string="Odoo Credit", currency_field="currency_id", default=0)
	sage_credit = fields.Monetary(string="Sage Credit", currency_field="currency_id", default=0)
	general_credit = fields.Monetary(string="General Credit", compute="_compute_credit")

	def _compute_credit(self):
		for record in self:
			record.general_credit = record.odoo_credit + record.sage_credit