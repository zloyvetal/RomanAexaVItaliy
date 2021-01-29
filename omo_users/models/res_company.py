# -*- coding: utf-8 -*-
# (C) 2020 OMO Systems (<"https://omo.systems/>)

from odoo import models, fields


class OmoUsersPartnerInherit(models.Model):
    """ Base class for model OMO Company """

    _inherit = 'res.company'

    omo_type = fields.Selection(related='partner_id.omo_type')
