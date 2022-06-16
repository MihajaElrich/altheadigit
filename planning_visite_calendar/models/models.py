# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class planning_visite_calendar(models.Model):
#     _name = 'planning_visite_calendar.planning_visite_calendar'
#     _description = 'planning_visite_calendar.planning_visite_calendar'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
