# -*- coding: utf-8 -*-

from odoo import models, fields

class milibro(models.Model):
    _name = 'milibro'
    _description = 'hola'
    titulo = fields.Char('Title', size=150, required=True)
    paginas = fields.Integer('Pages')
    autor = fields.Char('Author', size=150)
    editorial = fields.Char('Editorial', size=150)


milibro()

