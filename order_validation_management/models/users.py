# -*- coding : utf-8 -*-
from odoo import api, models, fields

class ResUsers(models.Model):
	_inherit = 'res.users'

	can_validate_order = fields.Boolean(string="Can Validate Order", default=False)