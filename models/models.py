# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class Cat(models.Model):
#     _name = 'cats.cat'
#     _description = 'Deskripsi Kucing'


#     name = fields.Char(string="Nama", required=True)
#     color = fields.Selection(selection=[
#         ('0', 'Merah'), ('1', 'Kuning'), ('2', 'Hijau'), ('3', 'Biru'), ('4', 'Ungu'), 
#     ], string="Warna", required=True)
#     type = fields.Many2one('cats.cat.type', string="Jenis")


# class CatType(models.Model):
#     _name = 'cats.cat.type'
#     _description = 'Jenis Kucing'


#     name = fields.Char(string="Nama")




# class Team(models.Model):
#     _name = 'middle.logging.team'
#     _description = 'team'

#     teamNumber = fields.Integer(string="team number")


  

# clientSatisfactionRate, taskWeightRate, effectivenessRate, effieciencyRate, note
class TeamActivity(models.Model):
        _name = 'middle.logging.team.activity'
        _description = 'team activity'

        # fake foreign key
        team = fields.Selection(selection=[
            ('1', 'tim 1'), ('2', 'tim 2'), ('3', 'tim 3'), ('4', 'tim 4'), ('5', 'tim 5')], string="team", required=True)
            
        clientSatisfactionRate = fields.Integer(string="clientSatisfactionRate", required=True)
        taskWeightRate = fields.Integer(string="taskWeightRate", required=True)
        effectivenessRate = fields.Integer(string="effectivenessRate", required=True)
        effieciencyRate = fields.Integer(string="effieciencyRate", required=True)
        note = fields.Char(string="note", required=False)



class ClientFeedback(models.Model):
        _name = 'middle.logging.client.feedback'
        _description = 'client feedback'


        mood = fields.Selection(selection=[
            ('5', 'Sangat Puas'), ('4', 'Puas'), ('3', 'Biasa Saja'), ('2', 'Tidak Puas'), ('1', 'Sangat Tidak Puas'), 
        ], string="Mood", required=True)
        note = fields.Char(string="note", required=False)


class WorkerActivity(models.Model):
    _name = 'middle.logging.worker.activity'
    _description = 'worker activity'

    # fake foreign key
    worker = fields.Selection(selection=[
        ('1', 'worker 1'), ('2', 'worker 2'), ('3', 'worker 3'), ('4', 'worker 4'), ('5', 'worker 5'),
    ], string="worker", required=True)

    # data
    activity = fields.Selection(selection=[
        ('1', 'Menyapu'), ('2', 'Berkebun'), ('3','Mencuci' )]
        , string="Activity", required=True)
    startTime = fields.Datetime(string="Start Time", required=True)
    endTime = fields.Datetime(string="End Time", required=True)
    rate = fields.Integer(string="Rate", required=True)
    note = fields.Char(string="Note", required=False)

