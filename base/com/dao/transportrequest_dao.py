from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.cropname_vo import CropNameVO
from base.com.vo.croprequest_vo import CropRequestVO
from base.com.vo.transportrequest_vo import TransportRequestVO


class TransportRequestDAO:
    def insert_transportrequest(self, transporrequest_vo):
        db.session.add(transporrequest_vo)
        db.session.commit()

    def user_view_transportrequest(self, transportrequest_vo):
        transportrequest_vo_list = TransportRequestVO.query \
            .filter_by(transportrequest_login_id=transportrequest_vo.transportrequest_login_id) \
            .all()
        return transportrequest_vo_list

    def admin_view_transportrequest(self):
        transportrequest_vo_list = TransportRequestVO.query.all()
        return transportrequest_vo_list

    def edit_croprequest(self, croprequest_vo):
        croprequest_vo_list = CropRequestVO.query.filter_by(croprequest_id=croprequest_vo.croprequest_id)
        return croprequest_vo_list

    def update_croprequest(self, croprequest_vo):
        db.session.merge(croprequest_vo)
        db.session.commit()

    def user_transportrequest_mail_details(self, transportrequest_vo):
        transportrequest_vo_list_mail_details = db.session.query(
            TransportRequestVO.transportrequest_id,
            TransportRequestVO.transportrequest_vehicle_type,
            TransportRequestVO.transportrequest_vehicle_number,
            TransportRequestVO.transportrequest_vehicle_charge,
            TransportRequestVO.transportrequest_login_id
        ).filter(
            TransportRequestVO.transportrequest_id == transportrequest_vo.transportrequest_id
        ).first()
        return transportrequest_vo_list_mail_details
