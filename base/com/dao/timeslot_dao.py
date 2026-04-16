from base import db
from base.com.vo.timeslot_vo import TimeSlotVO


class TimeSlotDAO:
    def insert_timeslot(self, timeslot_vo):
        db.session.add(timeslot_vo)
        db.session.commit()
        return "return"

    def admin_view_timeslot(self):
        timeslot_vo_list = TimeSlotVO.query.all()
        return timeslot_vo_list

    def user_view_timeslot(self):
        timeslot_vo_list = TimeSlotVO.query.all()
        return timeslot_vo_list

    def delete_timeslot(self, timeslot_vo):
        timeslot_vo_list = TimeSlotVO.query.get(timeslot_vo.timeslot_id)
        db.session.delete(timeslot_vo_list)
        db.session.commit()

    def edit_timeslot(self, timeslot_vo):
        timeslot_vo_list = TimeSlotVO.query.filter_by(timeslot_id=timeslot_vo.timeslot_id).all()
        return timeslot_vo_list

    def update_timeslot(self, timeslot_vo):
        db.session.merge(timeslot_vo)
        db.session.commit()

    def ajax_view_timeslot(self, timeslot_vo):
        timeslot_vo_list = TimeSlotVO.query.filter_by(timeslot_id=timeslot_vo.timeslot_id).all()
        return timeslot_vo_list