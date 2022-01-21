# -*- coding: utf-8 -*-

from odoo import models, fields


class milibro2_categorias(models.Model):
    _name = 'milibro2.categorias'
    name = fields.Char('Description', size=150, required=True)


milibro2_categorias()


class milibro2(models.Model):
    _name = 'milibro2'
    _inherit = 'milibro'
    _description = 'Esto es mi libro 2'
    isbn = fields.Char('ISBN', size=15)
    precio = fields.Float('Price', digits=(4,2))
    resumen = fields.Text('Description')
    fecha = fields.Date('Date')
    revisado = fields.Boolean('Revisado')
    aprobado = fields.Selection([('S','Si'),('N','No'),('P','Pendiente')],'Aprobado')
    categoria = fields.Many2one('milibro2.categorias','Category', ondelete='cascade')


milibro2()

