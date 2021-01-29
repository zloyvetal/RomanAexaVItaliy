from odoo import fields, models, api


class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    is_omo_device = fields.Boolean(string="OMO Device", related="product_id.is_omo_device")
    device_type = fields.Many2one("omo.device.type", related="product_id.device_type")
    group_of_device = fields.Selection([("personal", "Personal"), ("company", "Company")], string="Group device")
    who_added = fields.Many2one("res.partner", string="Who added")
    parent_id = fields.Many2one("stock.production.lot", string="Parent device")
    child_id = fields.One2many("stock.production.lot", string="Child device")
    #   homeid = fields.Char(string="Home ID")  # not approved
    address = fields.Char(string="Address")
    is_alive = fields.Boolean(string="IS ALIVE")
    status = fields.Selection([("on", "Settled"), ("off", "Not settled"), ("stock", "On stock"), ("dead", "Dead")],
                              string="Status", default="stock")
    client_ids = fields.Many2many('res.partner', string="Subscribers")
    info = fields.Text(string="Additional info")
    omo_create_time = fields.Datetime(string="Create time")
    omo_death_time = fields.Datetime(string="Death time")
    omo_deletion_time = fields.Datetime(string="Deleted")
    omo_last_activity_time  = fields.Datetime(string="Last activity")