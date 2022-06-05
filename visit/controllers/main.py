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

		return request.render("visit.visit_report", values)

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

	@http.route(['/shop/visit_report/save'], type='http', auth="public", website=True, sitemap=False)
	def save_visit(self, **post):
		order = request.website.sale_get_order()

		if post:
			if post.get('visit_id'):
				visit = request.env['visit'].browse(int(post.get('visit_id')))
				visit.update({
					'obj' : post.get('obj'),
					'start_datetime' : post.get('start_datetime').replace('T', ' '),
					'end_datetime' : post.get('end_datetime').replace('T', ' '),
					'result' : post.get('result'),					
					'competing_products' : post.get('competing_products'),					
					'marketing_watch' : post.get('marketing_watch'),					
				})

				# return request.redirect('/shop/payment/validate')
			else:
				visit = request.env['visit'].sudo().create({
					'obj' : post.get('obj'),
					'start_datetime' : post.get('start_datetime').replace('T', ' '),
					'end_datetime' : post.get('end_datetime').replace('T', ' '),
					'result' : post.get('result'),
					'competing_products' : post.get('competing_products'),
					'marketing_watch' : post.get('marketing_watch'),					
				})

				order.sudo().write({'visit' : visit.id})

				# return request.redirect('/shop/payment/validate')
			if order:
				order.with_context(send_email=True).action_confirm()
				# return request.redirect(order.get_portal_url())
				request.website.sale_reset()
				return request.redirect('/shop/end_order')
			# else:
			# 	return request.redirect('/shop/first_condition_not_true')
		else:
			return request.redirect('shop/address')

	@http.route(['/shop/end_order'], type='http', auth="public", website=True, sitemap=False)
	def end_order(self, **post):
		return request.render("visit.end_order")