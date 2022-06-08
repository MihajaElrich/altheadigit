# -*- coding : utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	def action_confirm(self):
		if not self.env.user.can_validate_order:
			raise UserError(_("You don't have the right to do this action"))
		else:
			super(SaleOrder, self).action_confirm()