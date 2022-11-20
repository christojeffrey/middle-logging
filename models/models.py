# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cat(models.Model):
    _name = 'cats.cat'
    _description = 'Deskripsi Kucing'


    name = fields.Char(string="Nama", required=True)
    color = fields.Selection(selection=[
        ('0', 'Merah'), ('1', 'Kuning'), ('2', 'Hijau'), ('3', 'Biru'), ('4', 'Ungu'), 
    ], string="Warna", required=True)
    type = fields.Many2one('cats.cat.type', string="Jenis")


class CatType(models.Model):
    _name = 'cats.cat.type'
    _description = 'Jenis Kucing'


    name = fields.Char(string="Nama")




class Team(models.Model):
    _name = 'middle.logging.team'
    _description = 'team'

    teamNumber = fields.Integer(string="team number")


  

# clientSatisfactionRate, taskWeightRate, effectivenessRate, effieciencyRate, note
# class TeamActivity(models.Model):
#         _name = '.team_activity'
#         _description = 'team activity'

#         team = fields.Integer(string="Team Number", required=True)
#         clientSatisfactionRate = fields.Integer(string="clientSatisfactionRate", required=True)
#         taskWeightRate = fields.Integer(string="taskWeightRate", required=True)
#         effectivenessRate = fields.Integer(string="effectivenessRate", required=True)
#         effieciencyRate = fields.Integer(string="effieciencyRate", required=True)
#         note = fields.Char(string="note", required=False)




