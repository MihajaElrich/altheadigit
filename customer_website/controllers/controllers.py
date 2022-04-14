# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CustomerSelection(http.Controller):
    @http.route('/website/customer_selection', auth='public', type='http')
    def index(self, **kw):
        Model = request.env['res.partner'].search([('id','=',kw.get('id'))])
        record = request.env.user

        values = {
            'customer_in_quotation_id': kw.get('id'),
            'customer_in_quotation_name': Model.name
        }
        record.write(values)

        return request.redirect('/shop')
    # @http.route('/customer_website/customer_website/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('customer_website.listing', {
    #         'root': '/customer_website/customer_website',
    #         'objects': http.request.env['customer_website.customer_website'].search([]),
    #     })

    # @http.route('/customer_website/customer_website/objects/<model("customer_website.customer_website"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('customer_website.object', {
    #         'object': obj
    #     })
