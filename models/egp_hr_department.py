from odoo import fields, models, api


class InheritedDepartment(models.Model):
    _inherit = "hr.department"

    organization_year = fields.Char(string='Creation Year')
    code = fields.Char(string='Code')
    position_rank_id = fields.Many2one('position.rank', string='Rank')
    position_status_id = fields.Many2one('position.status', string='Status')
    color = fields.Integer('Color Index', invisible=True)





