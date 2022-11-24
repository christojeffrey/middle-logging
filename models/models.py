# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TeamActivity(models.Model):
        _name = 'middle.logging.team.activity'
        _description = 'team activity'

        # fake foreign key
        team = fields.Selection(selection=[
            ('1', 'tim 1'), ('2', 'tim 2')], string="team", required=True)
            
        clientSatisfactionRate = fields.Selection(selection=[
            ('5', 'Sangat Puas'), ('4', 'Puas'), ('3', 'Biasa Saja'), ('2', 'Tidak Puas'), ('1', 'Sangat Tidak Puas'), 
        ], string="Mood", required=True)
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

# 1. tim ini ratingnya berapa
# 2. hari ini di mitra ini ngerjain apa aja
# 3. hari ini di tim di mitra ini ngerjain apa aja
# 4. seberapa puas client di mitra tertentu
# 5. average waktu yang dibutuhakn buat suatu pekerjaan
# 6. pekerjaan mana yang paling dapet tingkat kepuasan paling tinggi
# 7. pekerjaan mana yang paling dapet tingkat kepuasan paling rendah
class Statistics(models.Model):
    _name = "middle.logging.statistics"
    _description = "statistik"

    # data
    teamRating = fields.Char(string="Team Rating", required=False)        
    mitraActivity = fields.Char(string="Mitra Activity Today", required=False)
    teamActivity = fields.Char(string="Team Activity Today", required=False)
    clientSatisfaction = fields.Char(string="Mitra Satisfaction", required=False)
    averageTime = fields.Char(string="Average Time", required=False)
    bestJob = fields.Char(string="Best Job", required=False)
    worstJob = fields.Char(string="Worst Job", required=False)