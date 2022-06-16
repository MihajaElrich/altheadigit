# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerNifStat(models.Model):
    _inherit = 'res.partner'

    nif = fields.Char(string='NIF')
    stat = fields.Char(string='STAT')