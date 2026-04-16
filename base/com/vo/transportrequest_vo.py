import datetime
from base import db
from base.com.vo.cropname_vo import CropNameVO
from base.com.vo.login_vo import LoginVO


class TransportRequestVO(db.Model):
    __tablename__ = 'transportrequest_table'
    transportrequest_id = db.Column('transportrequest_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    transportrequest_vehicle_type = db.Column('transportrequest_vehicle_type', db.String(255),nullable=False )
    transportrequest_vehicle_number = db.Column('transportrequest_vehicle_number', db.String(255), nullable=False)
    transportrequest_vehicle_charge = db.Column('transportrequest_vehicle_charge', db.Integer,nullable=False)
    transportrequest_crop_name_id = db.Column('transportrequest_crop_name_id', db.Integer, db.ForeignKey(CropNameVO.crop_name_id))
    transportrequest_login_id = db.Column('transportrequest_login_id', db.Integer, db.ForeignKey(LoginVO.login_id))
    transportrequest_status = db.Column('transportrequest_status', db.String(20), nullable=False)
    transportrequest_date_time = db.Column('transportrequest_date_time', db.DateTime, default=datetime.datetime.now(), nullable=False)

    def as_dict(self):
        return {
            'transportrequest_id': self.transportrequest_id,
            'transportrequest_vehicle_type': self.transportrequest_vehicle_type,
            'transportrequest_vehicle_number': self.transportrequest_vehicle_number,
            'transportrequest_vehicle_charge': self.transportrequest_vehicle_charge,
            'transportrequest_login_id': self.transportrequest_login_id,
            'transportrequest_status': self.transportrequest_status,
            'transportrequest_date_time': self.transportrequest_date_time
        }


# db.create_all()