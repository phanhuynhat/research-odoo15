from email.policy import default
import string
from tkinter.tix import Select
from odoo import models, fields, api

class schoolinfo(models.Model):
    
    _name = 'school.information'
    _description = 'school.management'
    
    name = fields.Char(string='Tên trường')
    type = fields.Selection([('private','Dân lập'), ('public','Công lập')],default='public', string='Loại trường')
    email = fields.Text(string='Email')
    address = fields.Text(string='Địa chỉ')
    phoneNU = fields.Char(string='Số điện thoại')
    hasOnlineClass = fields.Boolean(string='Có lớp Online không')
    rank = fields.Integer(string='Xếp hạng')
    establishDay = fields.Date(string='Ngày thành lập')
    document = fields.Binary(string='Tài liệu trường')
    document_name = fields.Char(string='Tên tài liệu')  
    image = fields.Binary(string='Hình ảnh', attachment=True)
    
    class_list = fields.One2many('class.information', 'school_id', string='Danh sách lớp học')