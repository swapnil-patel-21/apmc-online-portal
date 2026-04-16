from base import db
from base.com.vo.booking_vo import BookingVO
from base.com.vo.timeslot_vo import TimeSlotVO
from base.com.vo.cropname_vo import CropNameVO


class BookingDAO:
    def insert_booking_slot(self, booking_vo):
        db.session.add(booking_vo)
        db.session.commit()

    def ajax_view_booking_slot(self, booking_vo):
        booking_vo_list = BookingVO.query \
            .filter_by(booking_timeslot_id = booking_vo.booking_timeslot_id, booking_date = booking_vo.booking_date) \
            .all()
        return booking_vo_list

    def admin_view_booking_slot(self):
        croprequest_vo_list = db.session.query(BookingVO, TimeSlotVO, CropNameVO) \
            .join(TimeSlotVO, BookingVO.booking_timeslot_id == TimeSlotVO.timeslot_id) \
            .join(CropNameVO, BookingVO.booking_name_id == CropNameVO.crop_name_id) \
            .all()
        return croprequest_vo_list

    def user_view_booking_slot(self, booking_vo):
        croprequest_vo_list = db.session.query(BookingVO, TimeSlotVO, CropNameVO) \
            .filter_by(booking_login_id=booking_vo.booking_login_id) \
            .join(TimeSlotVO, BookingVO.booking_timeslot_id == TimeSlotVO.timeslot_id) \
            .join(CropNameVO, BookingVO.booking_name_id == CropNameVO.crop_name_id) \
            .all()
        return croprequest_vo_list

    def update_booking(self, booking_vo):
        db.session.merge(booking_vo)
        db.session.commit()

