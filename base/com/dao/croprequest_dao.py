from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.cropname_vo import CropNameVO
from base.com.vo.croprequest_vo import CropRequestVO
from base.com.vo.transportrequest_vo import TransportRequestVO
from base.com.vo.booking_vo import BookingVO
from base.com.vo.timeslot_vo import TimeSlotVO
from base.com.vo.pricechart_vo import PriceChartVO
from base.com.vo.vehicle_vo import VehicleVO


class CropRequestDAO:
    def insert_croprequest(self, croprequest_vo):
        db.session.add(croprequest_vo)
        db.session.commit()

    def admin_view_croprequest(self):
        croprequest_vo_list = db.session.query(CropRequestVO, CropVO,CropNameVO) \
            .join(CropVO, CropRequestVO.croprequest_crop_type == CropVO.crop_id) \
            .join(CropNameVO, CropRequestVO.croprequest_crop_name == CropNameVO.crop_name_id) \
            .all()
        return croprequest_vo_list

    def user_view_croprequest(self, croprequest_vo):
        croprequest_vo_list = db.session.query(CropRequestVO, CropNameVO, CropVO) \
            .filter_by(croprequest_login_id=croprequest_vo.croprequest_login_id) \
            .join(CropNameVO, CropRequestVO.croprequest_crop_name == CropNameVO.crop_name_id) \
            .join(CropVO, CropRequestVO.croprequest_crop_type == CropVO.crop_id) \
            .all()
        return croprequest_vo_list

    def edit_croprequest(self, croprequest_vo):
        croprequest_vo_list = CropRequestVO.query.filter_by(croprequest_id=croprequest_vo.croprequest_id)
        return croprequest_vo_list

    def update_croprequest(self, croprequest_vo):
        db.session.merge(croprequest_vo)
        db.session.commit()


    def user_order_history(self, croprequest_vo):
        croprequest_vo_list = db.session.query(CropRequestVO, BookingVO, CropNameVO, CropVO, TimeSlotVO, PriceChartVO) \
            .filter_by(croprequest_login_id=croprequest_vo.croprequest_login_id) \
            .join(BookingVO, BookingVO.booking_name_id == CropRequestVO.croprequest_crop_name) \
            .join(CropNameVO, CropRequestVO.croprequest_crop_name == CropNameVO.crop_name_id) \
            .join(CropVO, CropRequestVO.croprequest_crop_type == CropVO.crop_id) \
            .join(TimeSlotVO, BookingVO.booking_timeslot_id == TimeSlotVO.timeslot_id) \
            .join(PriceChartVO, CropNameVO.crop_name_id == PriceChartVO.price_chart_crop_id) \
            .all()
        return croprequest_vo_list
