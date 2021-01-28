from odoo import fields, models, api


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    device_type = fields.Many2one('omo.device.type', string="Device type")

