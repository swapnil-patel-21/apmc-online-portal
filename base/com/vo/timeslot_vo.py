from base import db
import datetime

class TimeSlotVO(db.Model):
    __tablename__ = 'timeslot_table'
    timeslot_id = db.Column('timeslot_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    timeslot_type = db.Column('timeslot_type', db.String(255), nullable=False)
    timeslot_capacity = db.Column('timeslot_capacity', db.Integer, nullable=False)
    timeslot_date = db.Column(db.Date, default=datetime.date.today(), nullable=False)

    def as_dict(self):
        return {
            'timeslot_id': self.timeslot_id,
            'timeslot_type': self.timeslot_type,
            'timeslot_capacity': self.timeslot_capacity,
            'timeslot_date': self.timeslot_date
        }


# db.create_all()
