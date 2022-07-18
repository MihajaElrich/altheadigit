# -*- coding: utf-8 -*-
# from odoo import http


# class MonthlyTargetField(http.Controller):
#     @http.route('/monthly_target_field/monthly_target_field', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/monthly_target_field/monthly_target_field/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('monthly_target_field.listing', {
#             'root': '/monthly_target_field/monthly_target_field',
#             'objects': http.request.env['monthly_target_field.monthly_target_field'].search([]),
#         })

#     @http.route('/monthly_target_field/monthly_target_field/objects/<model("monthly_target_field.monthly_target_field"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('monthly_target_field.object', {
#             'object': obj
#         })
