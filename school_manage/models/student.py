from email.policy import default
from re import I
import string
import logging

_logger = logging.getLogger(__name__)
from unicodedata import name
from odoo import models, fields, api
from odoo.exceptions import UserError

class student(models.Model):
    
    _name = 'student.manage'
    _description = 'student management'
    
    name = fields.Char(string="Họ và tên", required=True)
    day_of_birth = fields.Date(string="Ngày sinh", required=True)
    # sex: fields.selection([('one','Nam'),('two','Nữ')], string='Giới tính')
    address = fields.Char(string="Địa chỉ", required=True)
    phone = fields.Char(string="Số điện thoại", required=True)
    class_id = fields.Many2one("class.manage", string="Lớp", required=True) 
    grade = fields.Char(related="class_id.grade", string="Khối")
    
    
    
    semester = fields.Integer(compute= "_compute_semester", string="Số học kỳ phải học")
    tuition = fields.Float(compute= "_auto_count_tuition", string='Học phí 1 kỳ')
    # tuition_sum = fields.Monetary(compute= "_compute_sum",string="Tổng số học phí") 
    
    @api.depends("grade")
    def _compute_semester(self):
        for re in self:
            if re.grade =="10":
                re.semester = 2
            elif re.grade == "11":
                re.semester = 3
            else:
                re.semester = 4
                
                
    
    @api.depends("semester")
    def _auto_count_tuition(self):
        for re in self:
            if re.semester =="2":
                re.tuition = "1000000"
            elif re.semester == "3":
                re.tuition = "2000000"
            else:
                re.tuition = "3000000"
                
                
    # @api.depends("semester", "tuition")
    # def _compute_sum(self):
    #     for re in self:
    #         re.tuition_sum= re.semester * re.tuition
            
    class Class(models.Model):
    
        _inherit = 'class.manage'
        
        student_list = fields.One2many("student.manage", "class_id", string="Danh sách học sinh")