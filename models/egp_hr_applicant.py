from odoo import api, fields, models


class Egp_hrApplicant(models.Model):
    _inherit = "hr.applicant"

    Father_name = fields.Char(string='Father Name')
    province = fields.Many2one('res.country.state', string="Province", tracking=True, ondelete='cascade')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')], tracking=True)
    LANGUAGES = [
        ('en_US', 'English (US)'),
        ('en_UK', 'English (UK)'),
        ('ps', 'Pashto'),
        ('prs', 'Dari'),
        ('other', 'Other'),
    ]
    native_language = fields.Selection(LANGUAGES, string='Native Language', default='ps')

    salary_proposed_extra = fields.Char("Proposed Salary Extra",
                                        help="Salary Proposed by the Organisation, extra advantages", tracking=True,
                                        groups="hr_recruitment.group_hr_recruitment_user,egp_hr.group_recruitment_amir,egp_hr.group_recruitment_Karshanas")
    salary_expected_extra = fields.Char("Expected Salary Extra", help="Salary Expected by Applicant, extra advantages",
                                        tracking=True,
                                        groups="hr_recruitment.group_hr_recruitment_user,egp_hr.group_recruitment_amir,egp_hr.group_recruitment_Karshanas")
    salary_proposed = fields.Float("Proposed Salary", group_operator="avg", help="Salary Proposed by the Organisation",
                                   tracking=True,
                                   groups="hr_recruitment.group_hr_recruitment_user,egp_hr.group_recruitment_amir,egp_hr.group_recruitment_Karshanas")
    salary_expected = fields.Float("Expected Salary", group_operator="avg", help="Salary Expected by Applicant",
                                   tracking=True,
                                   groups="hr_recruitment.group_hr_recruitment_user,egp_hr.group_recruitment_amir,egp_hr.group_recruitment_Karshanas")
    position_rank_id = fields.Many2one(related='job_id.position_rank_id', string='Position Rank', store=True)
    position_code = fields.Char(related='job_id.code', string='Job Code', store=True)