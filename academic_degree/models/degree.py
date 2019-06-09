from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class AcademicDegree(models.Model):
	_name = 'academic.degree'
	_description = 'Academic Degree'


	_inherit = ['mail.thread', 'mail.activity.mixin']

	name = fields.Char(string = "nama", required = True, track_visibility = "onchange", unique = True)
	description = fields.Html(string = "Deskripsi")
	active = fields.Boolean(string = "Aktif", default = True, track_visibility = "onchange")