from odoo import models, fields, api

class RoomMaster(models.Model):
    _name = 'room.master'
    _description = 'Room Master'
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Nama Ruangan harus unik!')
    ]

    name = fields.Char(string="Nama Ruangan", required=True)
    room_type = fields.Selection([
        ('small_meeting', 'Meeting Room Kecil'),
        ('large_meeting', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string="Tipe Ruangan", required=True)
    location = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')
    ], string="Lokasi Ruangan", required=True)
    photo = fields.Binary(string="Foto Ruangan", required=True)
    capacity = fields.Integer(string="Kapasitas Ruangan", required=True)
    description = fields.Text(string="Keterangan")
