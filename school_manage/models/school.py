from email.policy import default
import string
from tkinter.tix import Select
from odoo import models, fields, api

class school(models.Model):
    
    _name = 'school.manage'
    _description = 'school management'
    
    name = fields.Char(string='Tên trường')
    image = fields.Binary(string='Hình ảnh', attachment=True)
    email = fields.Text(string='Email')
    phoneNU = fields.Char(string='Số điện thoại')
    address = fields.Text(string='Địa chỉ')
    establishDay = fields.Date(string='Ngày thành lập')
    document = fields.Binary(string='Tài liệu trường')
    document_name = fields.Char(string='Tên tài liệu')  
    
    