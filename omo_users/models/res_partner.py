# -*- coding: utf-8 -*-
# (C) 2020 OMO Systems (<"https://omo.systems/>)

from odoo import models, fields


class OmoUsers(models.Model):
    """ Base class for model OMO User """

    _inherit = 'res.partner'

    devices_ids = fields.Many2many(
            'stock.production.lot',
            relation='omo_devices',
            column1='devices_id',
            column2='user_id',
            string='Devices')
    card_ids = fields.Many2many(
            'stock.production.lot',
            relation='omo_cards',
            column1='card_id',
            column2='user_id',
            string='Cards')
    hub_ids = fields.Many2many(
            'stock.production.lot',
            relation='omo_hubs',
            column1='hub_id',
            column2='user_id',
            string='Hubs')
    last_client_activity = fields.Datetime(string='Last Activity')
    omo_type = fields.Selection([('none', 'None'), ('done', 'Done')], string="OMO Type")
    related_company_id = fields.Many2one('res.company', string='Related Company')
    related_user_id = fields.Many2one('res.users', string='Related User')
    is_omo_client = fields.Boolean(string='Client')
