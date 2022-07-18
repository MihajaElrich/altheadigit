# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime

class DashboardTarget(models.Model):
    _name = 'dashboard.target'
    # _inherit = 'sale.order'

    @api.model
    def month_selection(self) :
        months = [
        ('1', 'Janvier'),
        ('2', 'Fevrier'),
        ('3', 'Mars'),
        ('4', 'Avril'),
        ('5', 'Mai'),
        ('6', 'Juin'),
        ('7', 'Juillet'),
        ('8', 'Aout'),
        ('9', 'Septembre'),
        ('10', 'Octobre'),
        ('11', 'Novembre'),
        ('12', 'Decembre')
        ]
        
        return months

    amount = fields.Float(string="Montant")
    type = fields.Selection([
        ('amount', 'Montant de commande'),
        ('target', 'Objectif')
        ], string='Type du montant')
    month = fields.Selection(month_selection, string='Mois')
    year = fields.Integer(string="Année")
    user_id = fields.Many2one('res.users', string='Vendeur', index=True, tracking=2, default=lambda self: self.env.user)
    current_user_id = fields.Integer(store=False, compute='_compute_current_user')

    def _compute_current_user(self) :
        return self.env.user.id

class DashboardParameter(models.Model):
    _name = 'dashboard.parameter'
    # _inherit = 'sale.order'

    @api.model
    def month_selection(self) :
        months = [
        ('1', 'Janvier'),
        ('2', 'Fevrier'),
        ('3', 'Mars'),
        ('4', 'Avril'),
        ('5', 'Mai'),
        ('6', 'Juin'),
        ('7', 'Juillet'),
        ('8', 'Aout'),
        ('9', 'Septembre'),
        ('10', 'Octobre'),
        ('11', 'Novembre'),
        ('12', 'Decembre')
        ]
        
        return months

    @api.model
    def year_selection(self) :
        years = [
            ('2022', '2022')
        ]
        
        return years

    def default_current_month(self) :
        now = fields.Datetime.now()
        _datenow = datetime.strptime(str(now), '%Y-%m-%d %H:%M:%S')
        return _datenow.month
    
    amount = fields.Float(string="Montant objectif")
    month = fields.Selection(month_selection, string='Mois', default=default_current_month)
    year = fields.Selection(year_selection, string="Année", default=2022)


    def init_dashboard(self):
        users = self.env['res.users'].search([('active', '=', True)])
        board_line = self.env['dashboard.target'].search([('id', '>', 0)])
        all_orders = self.env['sale.order'].search([('id', '>', 0)])
        if board_line :
            raise UserError("Unable to initialize, any lines already exists.")

        # get order's year
        orders_year = []
        for order in all_orders :
            _date = datetime.strptime(str(order.date_order), '%Y-%m-%d %H:%M:%S')
            if _date.year not in orders_year :
                orders_year.append( _date.year )


        # get order's month
        orders_month = []
        for order in all_orders :
            _date = datetime.strptime(str(order.date_order), '%Y-%m-%d %H:%M:%S')
            if _date.month not in orders_month :
                orders_month.append( _date.month )
                

        for user in users :
            orders = self.env['sale.order'].search([('user_id', '=', user.id), ('state', '=', 'sale')])

            vals = []

            # compute orders's amount for each year and month
            
            for year in orders_year :
                for month in orders_month :
                    orders_total_amount_of_month = 0
                    for order in orders :
                        order_date = datetime.strptime(str(order.date_order), '%Y-%m-%d %H:%M:%S')

                        if order_date.month == month and order_date.year == year :
                            orders_total_amount_of_month += order.amount_total

                    vals.append( {
                        "amount": orders_total_amount_of_month,
                        "type" : "amount", # Sale amount
                        "user_id": user.id,
                        "month": str(month),
                        "year": year
                    })

                    vals.append( {
                            "amount": self.get_target_amount(month, year) if user.customer_amount_target == 0 else user.customer_amount_target,
                            "type" : "target", # Target amount
                            "user_id": user.id,
                            "month": str(month),
                            "year": year
                    })

            dashboard = self.env['dashboard.target'].create(vals)

    def update_dashboard(self):
        users = self.env['res.users'].search([('active', '=', True)])
        board_line = self.env['dashboard.target'].search([('id', '>', 0)])
        all_orders = self.env['sale.order'].search([('id', '>', 0)])
        if not board_line :
            raise UserError("Unable to update, no lines detected in dashboard.")

        # get order's year
        orders_year = []
        for order in all_orders :
            _date = datetime.strptime(str(order.date_order), '%Y-%m-%d %H:%M:%S')
            if _date.year not in orders_year :
                orders_year.append( _date.year )


        # get order's month
        orders_month = []
        for order in all_orders :
            _date = datetime.strptime(str(order.date_order), '%Y-%m-%d %H:%M:%S')
            if _date.month not in orders_month :
                orders_month.append( _date.month )
                

        for user in users :
            orders = self.env['sale.order'].search([('user_id', '=', user.id), ('state', '=', 'sale')])

            # update orders's amount for each year and month
            
            for year in orders_year :
                for month in orders_month :

                    orders_total_amount_of_month = 0
                    for order in orders :
                        order_date = datetime.strptime(str(order.date_order), '%Y-%m-%d %H:%M:%S')

                        if order_date.month == month and order_date.year == year :
                            orders_total_amount_of_month += order.amount_total

                    # search 
                    amount_obj = self.env['dashboard.target'].search([
                        ('user_id', '=', user.id),
                        ('type', '=', 'amount'),
                        ('month', '=', str(month)),
                        ('year', '=', str(year))
                    ])
                    target_obj = self.env['dashboard.target'].search([
                        ('user_id', '=', user.id),
                        ('type', '=', 'target'),
                        ('month', '=', str(month)),
                        ('year', '=', str(year))
                    ])


                    if amount_obj and target_obj:
                        amount_vals = {
                            "amount": orders_total_amount_of_month
                        }
                        target_vals = {
                            "amount": self.get_target_amount(month, year) if user.customer_amount_target == 0 else user.customer_amount_target
                        }

                        # update dash row
                        amount_obj.write(amount_vals)
                        target_obj.write(target_vals)

                    elif not amount_obj and not target_obj :
                        amount_vals = {
                            "amount": orders_total_amount_of_month,
                            "type" : "amount", # Sale amount
                            "user_id": user.id,
                            "month": month,
                            "year": year
                        }
                        target_vals = {
                            "amount": self.get_target_amount(month, year) if user.customer_amount_target == 0 else user.customer_amount_target,
                            "type" : "target", # Target amount
                            "user_id": user.id,
                            "month": month,
                            "year": year
                        }
                        # Create dash row
                        self.env['dashboard.target'].create(amount_vals)
                        self.env['dashboard.target'].create(target_vals)
                    


    def get_target_amount(self, month, year) :
        
        row = self.search([('month', '=', str(month)), ('year', '=', str(year))])

        return row.amount if row else 0

