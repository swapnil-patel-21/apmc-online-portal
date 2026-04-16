import datetime
from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.cropname_vo import CropNameVO
from base.com.vo.login_vo import LoginVO


class CropRequestVO(db.Model):
    __tablename__ = 'croprequest_table'
    croprequest_id = db.Column('croprequest_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    croprequest_crop_type = db.Column('croprequest_crop_type', db.Integer, db.ForeignKey(CropVO.crop_id))
    croprequest_crop_name = db.Column('croprequest_crop_name', db.Integer, db.ForeignKey(CropNameVO.crop_name_id))
    croprequest_crop_quantity = db.Column('croprequest_crop_quantity', db.Integer)
    croprequest_crop_description = db.Column('croprequest_crop_description', db.String(255))
    croprequest_login_id = db.Column('croprequest_login_id', db.Integer, db.ForeignKey(LoginVO.login_id))
    croprequest_status = db.Column('croprequest_status', db.String(20), nullable=False)
    croprequest_date_time = db.Column('croprequest_date_time', db.DateTime, default=datetime.datetime.now(), nullable=False)

    def as_dict(self):
        return {
            'croprequest_id': self.croprequest_id,
            'croprequest_crop_type': self.croprequest_crop_type,
            'croprequest_crop_name': self.croprequest_crop_name,
            'croprequest_crop_quantity': self.croprequest_crop_quantity,
            'croprequest_crop_description': self.croprequest_crop_description,
            'croprequest_status': self.croprequest_status,
            'croprequest_date_time': self.croprequest_date_time
        }


# db.create_all()