# -*- coding: utf-8 -*-
# from odoo import http


# class SageDataSynchronization(http.Controller):
#     @http.route('/sage_data_synchronization/sage_data_synchronization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sage_data_synchronization/sage_data_synchronization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sage_data_synchronization.listing', {
#             'root': '/sage_data_synchronization/sage_data_synchronization',
#             'objects': http.request.env['sage_data_synchronization.sage_data_synchronization'].search([]),
#         })

#     @http.route('/sage_data_synchronization/sage_data_synchronization/objects/<model("sage_data_synchronization.sage_data_synchronization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sage_data_synchronization.object', {
#             'object': obj
#         })
