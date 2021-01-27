from odoo import fields, models, api


class OmoDevice(models.Model):
    _name = 'omo.device.type'
    _description = 'omo device type'

    name = fields.Char(string="Name")
#    type_model = fields.Char(string="Type model") - not approve
    code = fields.Char(string="Code")
    description = fields.Text(string="Description")
