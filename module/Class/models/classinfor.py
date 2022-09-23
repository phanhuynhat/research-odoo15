from email.policy import default
import string
from unicodedata import name
from odoo import models, fields, api

class ClassInformation(models.Model):
    
    _name = 'class.information'
    _description = 'class.management'
    
    name = fields.Char(string="Tên lớp", required=True)
    grade = fields.Char(string="Khối", required=True)
    mainTeacher = fields.Char(string="Giáo viên chủ nhiệm", required=True)
    school_id = fields.Many2one("school.information", string="Trường") 