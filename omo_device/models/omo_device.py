from odoo import fields, models, api


class OmoDevice(models.Model):
    _inherit = 'product.template'

    is_omo_device = fields.Boolean(string="OMO Device")
