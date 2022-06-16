# -*- coding: utf-8 -*-
# from odoo import http


# class VisitePlanning(http.Controller):
#     @http.route('/visite_planning/visite_planning', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/visite_planning/visite_planning/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('visite_planning.listing', {
#             'root': '/visite_planning/visite_planning',
#             'objects': http.request.env['visite_planning.visite_planning'].search([]),
#         })

#     @http.route('/visite_planning/visite_planning/objects/<model("visite_planning.visite_planning"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('visite_planning.object', {
#             'object': obj
#         })
