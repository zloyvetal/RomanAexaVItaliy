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
