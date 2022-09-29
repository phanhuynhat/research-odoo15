from email.policy import default
import string
from unicodedata import name
from odoo import models, fields, api

class Class(models.Model):
    
    _name = 'class.manage'
    _description = 'class management'
    
    name = fields.Char(string="Tên lớp", required=True)
    grade = fields.Char(compute="_auto_compute_grade", string="Khối", required=True)
    mainTeacher = fields.Char(string="Giáo viên chủ nhiệm", required=True)
    school_id = fields.Many2one("school.manage", string="Trường")
    
    @api.depends("name")
    def _auto_compute_grade(self):
        for re in self:
            if re.name == False:
                re.grade = ""
            else:
                re.grade = ''.join(list(re.name)[0:2])
    
    
    