from base import db
from base.com.vo.login_vo import LoginVO
from base.com.vo.user_vo import UserVO
from base.com.vo.crop_vo import CropVO
from base.com.vo.cropname_vo import CropNameVO
from base.com.vo.pricechart_vo import PriceChartVO
from base.com.vo.timeslot_vo import TimeSlotVO
from base.com.vo.booking_vo import BookingVO
from base.com.vo.complain_vo import ComplainVO
from base.com.vo.feedback_vo import FeedbackVO
from base.com.vo.croprequest_vo import CropRequestVO
from base.com.vo.transportrequest_vo import TransportRequestVO
from sqlalchemy import func
from datetime import date


class AdminDashboardDAO:

    def get_stats(self):
        avg = db.session.query(func.avg(FeedbackVO.feedback_rating)).scalar()
        return {
            'total_users':       db.session.query(LoginVO).filter_by(login_role='user').count(),
            'active_users':      db.session.query(LoginVO).filter_by(login_role='user', login_status='active').count(),
            'total_crop':        db.session.query(CropRequestVO).count(),
            'pending_crop':      db.session.query(CropRequestVO).filter_by(croprequest_status='Pending').count(),
            'total_transport':   db.session.query(TransportRequestVO).count(),
            'pending_transport': db.session.query(TransportRequestVO).filter_by(transportrequest_status='Pending').count(),
            'open_complaints':   db.session.query(ComplainVO).filter_by(complain_status='Pending').count(),
            'total_complaints':  db.session.query(ComplainVO).count(),
            'bookings_today':    db.session.query(BookingVO).filter_by(booking_date=date.today()).count(),
            'avg_rating':        round(float(avg), 1) if avg else 0.0,
            'crop_types':        db.session.query(CropVO).count(),
        }

    def get_recent_crop_requests(self):
        rows = db.session.query(CropRequestVO, LoginVO, CropNameVO)\
            .join(LoginVO, CropRequestVO.croprequest_login_id == LoginVO.login_id)\
            .join(CropNameVO, CropRequestVO.croprequest_crop_name == CropNameVO.crop_name_id)\
            .order_by(CropRequestVO.croprequest_date_time.desc()).limit(6).all()
        return [{
            'username':  l.login_username,
            'crop_name': cn.crop_name,
            'quantity':  r.croprequest_crop_quantity,
            'status':    r.croprequest_status,
            'datetime':  r.croprequest_date_time.strftime('%d %b %Y') if r.croprequest_date_time else '',
        } for r, l, cn in rows]

    def get_recent_transport(self):
        rows = db.session.query(TransportRequestVO, LoginVO)\
            .join(LoginVO, TransportRequestVO.transportrequest_login_id == LoginVO.login_id)\
            .order_by(TransportRequestVO.transportrequest_date_time.desc()).limit(5).all()
        return [{
            'username':       l.login_username,
            'vehicle_number': r.transportrequest_vehicle_number,
            'vehicle_type':   r.transportrequest_vehicle_type,
            'status':         r.transportrequest_status,
        } for r, l in rows]

    def get_recent_complaints(self):
        rows = db.session.query(ComplainVO, LoginVO)\
            .join(LoginVO, ComplainVO.complain_from_login_id == LoginVO.login_id)\
            .order_by(ComplainVO.complain_datetime.desc()).limit(5).all()
        return [{
            'from':     l.login_username,
            'subject':  c.complain_subject,
            'status':   c.complain_status,
            'datetime': c.complain_datetime.strftime('%d %b %Y') if c.complain_datetime else '',
        } for c, l in rows]

    def get_price_chart(self):
        rows = db.session.query(PriceChartVO, CropNameVO)\
            .join(CropNameVO, PriceChartVO.price_chart_crop_id == CropNameVO.crop_name_id)\
            .order_by(PriceChartVO.crop_price_date.desc()).limit(6).all()
        return [{
            'crop_name': cn.crop_name,
            'price':     p.crop_price,
            'date':      str(p.crop_price_date),
        } for p, cn in rows]

    def get_all_users(self):
        rows = db.session.query(UserVO, LoginVO)\
            .join(LoginVO, UserVO.user_login_id == LoginVO.login_id).limit(6).all()
        return [{
            'name':     f'{u.user_firstname} {u.user_lastname}',
            'username': l.login_username,
            'status':   l.login_status,
        } for u, l in rows]

    def get_recent_feedback(self):
        rows = db.session.query(FeedbackVO, LoginVO)\
            .join(LoginVO, FeedbackVO.feedback_login_id == LoginVO.login_id)\
            .order_by(FeedbackVO.feedback_datetime.desc()).limit(5).all()
        return [{
            'username':    l.login_username,
            'rating':      f.feedback_rating,
            'description': f.feedback_description,
            'datetime':    f.feedback_datetime.strftime('%d %b %Y') if f.feedback_datetime else '',
        } for f, l in rows]


class UserDashboardDAO:

    def get_stats(self, login_id):
        return {
            'crop_requests':  db.session.query(CropRequestVO).filter_by(croprequest_login_id=login_id).count(),
            'transport_reqs': db.session.query(TransportRequestVO).filter_by(transportrequest_login_id=login_id).count(),
            'bookings':       db.session.query(BookingVO).filter_by(booking_login_id=login_id).count(),
            'complaints':     db.session.query(ComplainVO).filter_by(complain_from_login_id=login_id).count(),
        }

    def get_my_crop_requests(self, login_id):
        rows = db.session.query(CropRequestVO, CropNameVO, CropVO)\
            .join(CropNameVO, CropRequestVO.croprequest_crop_name == CropNameVO.crop_name_id)\
            .join(CropVO, CropRequestVO.croprequest_crop_type == CropVO.crop_id)\
            .filter(CropRequestVO.croprequest_login_id == login_id)\
            .order_by(CropRequestVO.croprequest_date_time.desc()).limit(5).all()
        return [{
            'crop_name': cn.crop_name,
            'crop_type': ct.crop_type,
            'quantity':  r.croprequest_crop_quantity,
            'status':    r.croprequest_status,
            'datetime':  r.croprequest_date_time.strftime('%d %b %Y') if r.croprequest_date_time else '',
        } for r, cn, ct in rows]

    def get_my_transport(self, login_id):
        rows = db.session.query(TransportRequestVO)\
            .filter_by(transportrequest_login_id=login_id)\
            .order_by(TransportRequestVO.transportrequest_date_time.desc()).limit(4).all()
        return [{
            'vehicle_type':   r.transportrequest_vehicle_type,
            'vehicle_number': r.transportrequest_vehicle_number,
            'status':         r.transportrequest_status,
            'datetime':       r.transportrequest_date_time.strftime('%d %b %Y') if r.transportrequest_date_time else '',
        } for r in rows]

    def get_my_bookings(self, login_id):
        rows = db.session.query(BookingVO, TimeSlotVO)\
            .join(TimeSlotVO, BookingVO.booking_timeslot_id == TimeSlotVO.timeslot_id)\
            .filter(BookingVO.booking_login_id == login_id)\
            .order_by(BookingVO.booking_date.desc()).limit(4).all()
        return [{
            'slot':   s.timeslot_type,
            'date':   str(b.booking_date),
            'status': b.booking_status,
        } for b, s in rows]

    def get_my_complaints(self, login_id):
        rows = db.session.query(ComplainVO)\
            .filter_by(complain_from_login_id=login_id)\
            .order_by(ComplainVO.complain_datetime.desc()).limit(4).all()
        return [{
            'subject':  c.complain_subject,
            'status':   c.complain_status,
            'reply':    c.complain_reply_description or '—',
            'datetime': c.complain_datetime.strftime('%d %b %Y') if c.complain_datetime else '',
        } for c in rows]

    def get_price_chart(self):
        rows = db.session.query(PriceChartVO, CropNameVO)\
            .join(CropNameVO, PriceChartVO.price_chart_crop_id == CropNameVO.crop_name_id)\
            .order_by(PriceChartVO.crop_price_date.desc()).limit(6).all()
        return [{
            'crop_name': cn.crop_name,
            'price':     p.crop_price,
            'date':      str(p.crop_price_date),
        } for p, cn in rows]

    def get_available_slots(self):
        rows = db.session.query(TimeSlotVO)\
            .filter(TimeSlotVO.timeslot_date >= date.today())\
            .order_by(TimeSlotVO.timeslot_date).limit(6).all()
        result = []
        for s in rows:
            booked = db.session.query(BookingVO)\
                .filter_by(booking_timeslot_id=s.timeslot_id).count()
            result.append({
                'id':        s.timeslot_id,
                'type':      s.timeslot_type,
                'date':      str(s.timeslot_date),
                'capacity':  s.timeslot_capacity,
                'available': max(0, s.timeslot_capacity - booked),
            })
        return result

    def get_profile(self, login_id):
        u = db.session.query(UserVO).filter_by(user_login_id=login_id).first()
        if not u:
            return {}
        return {
            'firstname': u.user_firstname,
            'lastname':  u.user_lastname,
            'gender':    u.user_gender,
            'address':   u.user_address,
            'contact':   u.user_contactnumber,
        }