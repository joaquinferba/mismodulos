# -*- coding: utf-8 -*-
# from odoo import http


# class Milibro2(http.Controller):
#     @http.route('/milibro2/milibro2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/milibro2/milibro2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('milibro2.listing', {
#             'root': '/milibro2/milibro2',
#             'objects': http.request.env['milibro2.milibro2'].search([]),
#         })

#     @http.route('/milibro2/milibro2/objects/<model("milibro2.milibro2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('milibro2.object', {
#             'object': obj
#         })
