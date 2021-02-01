
from odoo import models, fields, api, exceptions


class StockProductionLotInherit(models.Model):
    _inherit = "stock.production.lot"

    log_ids = fields.One2many('omo.logs', 'device_id', string="Logs ")


