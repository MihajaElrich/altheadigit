# -*- coding: utf-8 -*-
# from odoo import http


# class RestrictSaleDiscount(http.Controller):
#     @http.route('/restrict_sale_discount/restrict_sale_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restrict_sale_discount/restrict_sale_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('restrict_sale_discount.listing', {
#             'root': '/restrict_sale_discount/restrict_sale_discount',
#             'objects': http.request.env['restrict_sale_discount.restrict_sale_discount'].search([]),
#         })

#     @http.route('/restrict_sale_discount/restrict_sale_discount/objects/<model("restrict_sale_discount.restrict_sale_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restrict_sale_discount.object', {
#             'object': obj
#         })
