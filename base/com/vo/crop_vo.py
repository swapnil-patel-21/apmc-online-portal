from base import db


class CropVO(db.Model):
    __tablename__ = 'crop_table'
    crop_id = db.Column('crop_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    crop_type = db.Column('crop_type', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'crop_id': self.crop_id,
            'crop_type': self.crop_type
        }


# db.create_all()
