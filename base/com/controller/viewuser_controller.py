from flask import *

from base import app
from base.com.vo.user_vo import UserVO
from base.com.dao.user_dao import UserDAO
from base.com.controller.login_controller import admin_login_session, admin_logout_session


@app.route('/admin/view_user', methods=['GET'])
def admin_view_user():
    """ Admin view user function """
    try:
        if admin_login_session() == 'admin':

            user_vo = UserVO()
            user_dao = UserDAO()
            user_vo_list = user_dao.search_user()

            return render_template('admin/viewUser.html', user_vo_list=user_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_user route exception occured>>>>>>>>>>", ex)