from odoo import fields, models, api


class Egp_hrEmployee(models.Model):
    _inherit = "hr.employee"

    message_main_attachment_id = fields.Many2one(
        groups="hr.group_hr_user,egp_hr.group_recruitment_Karshanas,egp_hr.group_recruitment_amir,base.group_erp_manager")
    issue_date = fields.Char(string='Issue Date')
    expire_date = fields.Char(string='Expire Date')
    pashto_position_Title = fields.Char(string='Pashto/Farsi Position Title', required=True)
    Employee_pashto_name = fields.Char(string=' Pashto/Farsi Employee Name', required=True)
    barcode = fields.Char(string="Badge ID", help="ID used for employee identification.", groups="hr.group_hr_user,egp_hr.group_recruitment_amir,egp_hr.group_recruitment_Karshanas",  copy=False)
