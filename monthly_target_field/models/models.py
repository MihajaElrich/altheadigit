# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MonthlyTargetField(models.Model):
    _inherit = 'sale.order'

    month_target = fields.Float(string="Objectif du mois", compute="_compute_month_target")

    def _compute_month_target(self) :
        self.month_target = [1.0, 2.0]
    
