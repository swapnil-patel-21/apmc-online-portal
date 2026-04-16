from flask import *
from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.croprequest_dao import CropRequestDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.timeslot_dao import TimeSlotDAO
from base.com.vo.croprequest_vo import CropRequestVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.timeslot_vo import TimeSlotVO


@app.route('/user/load_view_receipt', methods=['GET'])
def user_view_receipt():
    """ User view receipt function """
    try:
        if admin_login_session() == 'user':

            login_vo = LoginVO()
            login_dao = LoginDAO()
            croprequest_vo = CropRequestVO()
            croprequest_dao = CropRequestDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            croprequest_vo.croprequest_login_id = login_id
            receipt_vo_list = croprequest_dao.user_order_history(croprequest_vo)
            print(receipt_vo_list)

            return render_template('user/viewReceipt.html', receipt_vo_list=receipt_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_view_receipt route exception occured>>>>>>>>>>", ex)