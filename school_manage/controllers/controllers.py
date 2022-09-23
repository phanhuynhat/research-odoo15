# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolManage(http.Controller):
#     @http.route('/school_manage/school_manage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_manage/school_manage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_manage.listing', {
#             'root': '/school_manage/school_manage',
#             'objects': http.request.env['school_manage.school_manage'].search([]),
#         })

#     @http.route('/school_manage/school_manage/objects/<model("school_manage.school_manage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_manage.object', {
#             'object': obj
#         })
