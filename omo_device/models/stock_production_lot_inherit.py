from odoo import fields, models, api


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    is_omo_device = fields.Boolean(string="OMO Device", related="product_id.is_omo_device")
    device_type = fields.Many2one("omo.device.type", related="product_id.device_type")

