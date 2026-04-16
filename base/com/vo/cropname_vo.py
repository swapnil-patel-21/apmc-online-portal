from base import db
from base.com.vo.crop_vo import CropVO


class CropNameVO(db.Model):
    __tablename__ = 'crop_name_table'
    crop_name_id = db.Column('crop_name_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    crop_name = db.Column('crop_name', db.String(255), nullable=False)
    crop_description = db.Column('crop_description', db.String(500), nullable=False)
    crop_type_id = db.Column('crop_type_id', db.Integer, db.ForeignKey(CropVO.crop_id))


    def as_dict(self):
        return {
            'crop_name_id': self.crop_name_id,
            'crop_name': self.crop_name,
            'crop_description': self.crop_description,
            'crop_type_id':self.crop_type_id
        }


# db.create_all()
