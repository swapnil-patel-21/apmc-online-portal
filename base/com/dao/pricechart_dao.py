from base import db
from base.com.vo.cropname_vo import CropNameVO
from base.com.vo.crop_vo import CropVO
from base.com.vo.pricechart_vo import PriceChartVO


class PriceChartDAO:
    def insert_price(self, price_chart_vo):
        db.session.add(price_chart_vo)
        db.session.commit()

    def admin_view_price(self):
        price_chart_vo_list = db.session.query(PriceChartVO, CropNameVO) \
            .join(CropNameVO, PriceChartVO.price_chart_crop_id == CropNameVO.crop_name_id) \
            .all()
        return price_chart_vo_list

    def user_view_price(self):
        price_chart_vo_list = db.session.query(PriceChartVO, CropNameVO) \
            .join(CropNameVO, PriceChartVO.price_chart_crop_id == CropNameVO.crop_name_id) \
            .all()
        return price_chart_vo_list

    def delete_price(self, price_chart_vo):
        price_chart_vo_list = PriceChartVO.query.get(price_chart_vo.price_chart_id)
        db.session.delete(price_chart_vo_list)
        db.session.commit()

    def edit_price(self, price_chart_vo):
        price_chart_vo_list = db.session.query(PriceChartVO, CropNameVO, CropVO)\
            .filter_by(price_chart_id=price_chart_vo.price_chart_id) \
            .join(CropNameVO, PriceChartVO.price_chart_crop_id == CropNameVO.crop_name_id) \
            .all()
        return price_chart_vo_list

    def update_price(self, price_chart_vo):
        db.session.merge(price_chart_vo)
        db.session.commit()
