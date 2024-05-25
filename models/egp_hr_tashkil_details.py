from odoo import fields, models, api


class TashkilDetails(models.Model):
    _name = "tashkil.details"

    organization_year = fields.Char(string='Year')
    code = fields.Char(string='Code')
    position_rank_id = fields.Many2one('position.rank', string='Rank')
    position_status_id = fields.Many2one('position.status', string='Status')
    position_ids = fields.Many2one('hr.job', string='Job Positions')
    tashkil_ids = fields.Many2one('egp_hr.tashkil')
