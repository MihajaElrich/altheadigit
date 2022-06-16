# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VisitePlanning(models.Model):
    _inherit = 'calendar.event'

    customer_id = fields.Many2one(
        'res.partner', string='Client', readonly=False)
    # partner_ids = fields.Many2many(
    #     'res.partner', 'calendar_event_res_partner_rel',
    #     string='Attendees', default=_default_partners, domain="[('user_ids', '!=', None)]")

    @api.onchange('customer_id')
    def change_customer(self):
        # SET NAME TO Customer's name
        self.name = self.customer_id.name
        # _partner_ids = [self.customer_id.id, self.user_id.partner_id.id ]
        # self.update({
        #     'partner_ids': [( 6, 0, _partner_ids)]
        # })
        

