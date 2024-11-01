from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class RoomBooking(models.Model):
    _name = 'room.booking'
    _description = 'Room Booking'
    _order = 'booking_number'
    _sql_constraints = [
        ('unique_booking_room_date', 'unique(room_id, booking_date)', 'Ruangan tidak boleh dipesan untuk tanggal yang sama!'),
        ('unique_booking_name', 'unique(booking_name)', 'Nama Pemesanan harus unik!')
    ]

    booking_number = fields.Char(string="Nomor Pemesanan", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    room_id = fields.Many2one('room.master', string="Ruangan", required=True)
    booking_name = fields.Char(string="Nama Pemesan", required=True)
    booking_date = fields.Date(string="Tanggal Pemesanan", required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], string="Status Pemesanan", default='draft')
    notes = fields.Text(string="Catatan Pemesanan")

    @api.model
    def create(self, vals):
        if vals.get('booking_number', _('New')) == _('New'):
            vals['booking_number'] = self.env['ir.sequence'].next_by_code('room.booking') or _('New')
        return super(RoomBooking, self).create(vals)

    def action_process(self):
        self.ensure_one()
        if self.status == 'draft':
            self.status = 'ongoing'
        elif self.status == 'ongoing':
            self.status = 'done'
        else:
            raise ValidationError(_('Pemesanan sudah selesai.'))

    @api.constrains('room_id', 'booking_date')
    def _check_booking_conflict(self):
        for record in self:
            existing_booking = self.search([
                ('room_id', '=', record.room_id.id),
                ('booking_date', '=', record.booking_date),
                ('id', '!=', record.id)
            ])
            if existing_booking:
                raise ValidationError(_("Ruangan tidak bisa dipesan untuk tanggal yang sama."))
