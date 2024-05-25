from odoo import fields, models, api


class TashkilDetails(models.Model):
    _name = "tashkil.details"

    egp_tashkil_id = fields.Many2one('egp.tashkil', string='Tashkil Details', invisible=True)
    inherited_job_id = fields.Many2one('hr.job', string='Job Position')
    organization_year = fields.Char(related='inherited_job_id.organization_year', string='Creation Year')
    code = fields.Char(related='inherited_job_id.code', string='Code')
    color_inherited = fields.Integer(related='inherited_job_id.color', string='color')
    position_rank_id = fields.Many2one('position.rank', string='Rank')
    position_status_id = fields.Many2one('position.status', string='Status')
    inherited_department_id = fields.Many2one('hr.department', string='Department')
