# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerNifStat(http.Controller):
#     @http.route('/partner_nif_stat/partner_nif_stat', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_nif_stat/partner_nif_stat/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_nif_stat.listing', {
#             'root': '/partner_nif_stat/partner_nif_stat',
#             'objects': http.request.env['partner_nif_stat.partner_nif_stat'].search([]),
#         })

#     @http.route('/partner_nif_stat/partner_nif_stat/objects/<model("partner_nif_stat.partner_nif_stat"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_nif_stat.object', {
#             'object': obj
#         })
