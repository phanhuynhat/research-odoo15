from email.policy import default
from re import I
import string
import logging

_logger = logging.getLogger(__name__)
from unicodedata import name
from odoo import models, fields, api
from odoo.exceptions import UserError

class StudentInformation(models.Model):
    
    _name = 'student.information'
    _description = 'student.management'
    
    name = fields.Char(string="Họ và tên", required=True)
    day_of_birth = fields.Date(string="Ngày sinh", required=True)
    class_id = fields.Many2one("class.information", string="Lớp", required=True) 
    school_id = fields.Many2one("school.information", string="Trường") 
    subject_list = fields.Many2many("subject.information", "relation_subject_student", "student_id", "subject_id", string="Môn học")
    
    def write(self, values):
        rtn = super(StudentInformation, self).write(values)
        print(self.subject_list)
        for i in self.subject_list:
            if 9 == i:
                return rtn
            else:
                raise UserError("Anh là môn học bắt buộc, anhvkt456")
        return rtn


class ClassInformation(models.Model):
    
    _inherit = 'class.information'
    
    student_list = fields.One2many("student.information", "class_id", string="Danh sách học sinh")
    
class SubjectInformation(models.Model):
    _name = "subject.information"
    _description = "Subject information"
    
    name = fields.Char(string="Tên môn học")
    teachers = fields.Char(string="Giáo viên dạy")