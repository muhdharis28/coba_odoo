from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class AcademicMajor(models.Model):
	_name = 'academic.major'
	_description = 'Academic Major'


	_inherit = ['mail.thread', 'mail.activity.mixin']

	name = fields.Char(string = "Nama", required = True, track_visibility = "onchange", unique = True)
	code = fields.Char(string = "Code", required = True, track_visibility = "onchange", unique = True)
	description = fields.Html(string = "Deskripsi")
	seq = fields.Integer(string = "Sequence", required = True)
	academic_title_prefix = fields.Char(string = "Academic Title Prefix", required = True)
	academic_title_suffix = fields.Char(string = "Academic Title Sufix", required = True)
	active = fields.Boolean(string = "Aktif", default = True, track_visibility = "onchange")
	degree_id = fields.Many2one('academic.degree', string = "Degree", required = True, ondelete = "restrict", onupdate = "restrict")