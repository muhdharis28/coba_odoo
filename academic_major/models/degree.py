from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class AcademicDegree(models.Model):
	_inherit = 'academic.degree'
	major_ids = fields.One2many('academic.major', 'degree_id', string = "Jurusan Terkait")