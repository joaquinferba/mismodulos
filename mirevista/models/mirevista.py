# -*- coding: utf-8 -*-

from odoo import models, fields


class mirevista(models.Model):
    _name = 'mirevista'
    titulo = fields.Char('Title', size=15)
    categoria = fields.Many2one('milibro2.categorias','Category', ondelete='Cascade')


mirevista()


