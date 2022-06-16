# -*- coding: utf-8 -*-
# from odoo import http


# class PlanningVisiteCalendar(http.Controller):
#     @http.route('/planning_visite_calendar/planning_visite_calendar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/planning_visite_calendar/planning_visite_calendar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('planning_visite_calendar.listing', {
#             'root': '/planning_visite_calendar/planning_visite_calendar',
#             'objects': http.request.env['planning_visite_calendar.planning_visite_calendar'].search([]),
#         })

#     @http.route('/planning_visite_calendar/planning_visite_calendar/objects/<model("planning_visite_calendar.planning_visite_calendar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('planning_visite_calendar.object', {
#             'object': obj
#         })
