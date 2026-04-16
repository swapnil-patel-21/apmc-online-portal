from base import db
from base.com.vo.login_vo import LoginVO
from base.com.vo.timeslot_vo import TimeSlotVO
import datetime


class BookingVO(db.Model):
    __tablename__ = 'booking_table'
    booking_id = db.Column('booking_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    booking_name_id = db.Column('booking_name_id', db.String(255), nullable=False)
    booking_date = db.Column('booking_date', db.Date, nullable=False)
    booking_login_id = db.Column('booking_login_id', db.Integer, db.ForeignKey(LoginVO.login_id))
    booking_timeslot_id = db.Column('booking_timeslot_id', db.Integer, db.ForeignKey(TimeSlotVO.timeslot_id))
    booking_status = db.Column('booking_status', db.String(20), nullable=False)

    def as_dict(self):
        return {
            'booking_id': self.booking_id,
            'booking_name_id': self.booking_name_id,
            'booking_date': self.booking_date,
            'booking_login_id': self.booking_login_id,
            'booking_timeslot_id': self.booking_timeslot_id,
            'booking_status': self.booking_status
        }

# db.create_all()