import datetime

from base import db
from base.com.vo.cropname_vo import CropNameVO


class PriceChartVO(db.Model):
    __tablename__ = 'price_chart_table'
    price_chart_id = db.Column('price_chart_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    crop_price = db.Column('crop_price', db.Integer, nullable=False)
    price_chart_crop_id = db.Column('price_chart_crop_id', db.Integer, db.ForeignKey(CropNameVO.crop_name_id))
    crop_price_date = db.Column('crop_price_date', db.Date, default= datetime.datetime.now(), nullable=False)

    def as_dict(self):
        return {
            'price_chart_id': self.price_chart_id,
            'crop_price': self.crop_price,
            'price_chart_crop_id': self.price_chart_crop_id,
            'crop_price_date_time': self.crop_price_date
        }


# db.create_all()