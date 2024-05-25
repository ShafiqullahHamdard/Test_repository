from odoo import models, fields, api


class PositionRank(models.Model):
    _name = 'position.rank'
    _description = 'Position Rank'
    _inherit = ['mail.thread']
    _rec_name = 'position_rank'

    position_rank = fields.Char(string='Rank', required=True)
