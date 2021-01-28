# -*- coding: utf-8 -*-
# (C) 2021 OMO Systems (<"https://omo.systems/>)

from odoo import models, fields, api, exceptions


class OmoLogs(models.Model):
    _name = 'omo.logs'
    _description = 'Omo logs'

    company_id = fields.Many2one('res.company', string='Company')
    correlationid = fields.Char(string="Correlation ID")
    log_severity = fields.Selection(
        string='Severity',
        selection=[('info', 'INFO'),
                   ('', ''),
                   ],
    )
    timestamp = fields.Char(string="Timestamp")
    msg = fields.Text(string="Message")
    device_id = fields.Many2one('stock.production.lot', string='Device')
    hub_id = fields.Many2one('stock.production.lot', string='Parent device')
    product_id = fields.Many2one('product.product', related='device_id.product_id', string='Product')
    device_type = fields.Many2one('omo.device.type', related='device_id.device_type', string='Device type')
