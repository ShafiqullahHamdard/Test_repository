from odoo import fields, models, api


class Tashkil(models.Model):
    _name = 'egp.tashkil'
    _description = 'Tashkil Model'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name')
    tashkil_year = fields.Integer(string='Tashkil Year')
    sequence_number = fields.Char(string='Sequence Number', readonly=False)
    description = fields.Text(string='Description')
    job_position_ids = fields.One2many('tashkil.details', 'egp_tashkil_id', string='Job Details')

    @api.onchange('sequence_number')
    def _onchange_sequence_number(self):
        prefix = 'MCIT/AF-'
        self.sequence_number = prefix + self.sequence_number if self.sequence_number else ''

    def copy(self, default=None):
        # Duplicate the main record
        new_tashkil = super(Tashkil, self).copy(default=default)

        # Duplicate related job_position_ids records
        for job_position in self.job_position_ids:
            job_position.copy({'egp_tashkil_id': new_tashkil.id})

        return new_tashkil
