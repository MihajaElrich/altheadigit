# -*- coding: utf-8 -*-

from odoo.exceptions import UserError
from odoo import models, fields, api

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def write(self, vals):
        # print(str(vals))
        # if 'state' in vals:
        #     # if vals['state'] == "sent" and self.website_id.id == 1 :
        #         # 
        vals['partner_id'] = self.env.user.customer_in_quotation_id
        vals['partner_invoice_id'] = self.env.user.customer_in_quotation_id
        return super(SaleOrder, self).write(vals)

    # @api.models
    # def create(self, vals):
    #     vals['partner_id'] = self.env.user.customer_in_quotation_id
    #     vals['partner_invoice_id'] = self.env.user.customer_in_quotation_id
    #     rec = super(SaleOrder, self).create(vals)
        
    #     return rec
    
