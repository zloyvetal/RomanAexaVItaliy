# -*- coding: utf-8 -*-
# (C) 2020 OMO Systems (<"https://omo.systems/>)

from odoo import models, fields


class OmoUsersUserInherit(models.Model):
    ''' Base class OMO User of omo system '''

    _inherit = 'res.users'

    additional_info = fields.Text(string='Additional info')
    access_token = fields.Char(string='Access token')
    userid = fields.Char(string='User ID')
    phone = fields.Char(srting='Phone')
