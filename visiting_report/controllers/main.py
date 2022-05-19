# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSale(WebsiteSale):
	@http.route(['/shop/visit_report'], type='http', auth="public", website=True, sitemap=False)
	def visit_report(self, **post):
		order = request.website.sale_get_order()

		values = self.checkout_values(**post)

		values.update({'website_sale_order' : order})

		return request.render("visiting_report.visit_report", values)

	@http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
	def checkout(self, **post):
		order = request.website.sale_get_order()

		redirection = self.checkout_redirection(order)
		if redirection:
			return redirection

		if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
			return request.redirect('/shop/address')

		redirection = self.checkout_check_address(order)
		if redirection:
			return redirection

		values = self.checkout_values(**post)

		if post.get('express'):
			return request.redirect('/shop/visit_report')

		values.update({'website_sale_order': order})

		# Avoid useless rendering if called in ajax
		if post.get('xhr'):
			return 'ok'
		return request.render("website_sale.checkout", values)