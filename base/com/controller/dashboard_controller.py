from flask import *
from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.dashboard_dao import AdminDashboardDAO, UserDashboardDAO
from base.com.dao.login_dao import LoginDAO
from base.com.vo.login_vo import LoginVO


# ── ADMIN DASHBOARD ────────────────────────────────────────────

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/index.html')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_dashboard exception >>>>>>>>>>", ex)


@app.route('/admin/dashboard/stats', methods=['GET'])
def admin_dashboard_stats():
    try:
        if admin_login_session() == 'admin':
            dao = AdminDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_stats()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("admin_dashboard_stats exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/admin/dashboard/crop_requests', methods=['GET'])
def admin_dashboard_crop_requests():
    try:
        if admin_login_session() == 'admin':
            dao = AdminDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_recent_crop_requests()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("admin_dashboard_crop_requests exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/admin/dashboard/transport_requests', methods=['GET'])
def admin_dashboard_transport_requests():
    try:
        if admin_login_session() == 'admin':
            dao = AdminDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_recent_transport()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("admin_dashboard_transport_requests exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/admin/dashboard/complaints', methods=['GET'])
def admin_dashboard_complaints():
    try:
        if admin_login_session() == 'admin':
            dao = AdminDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_recent_complaints()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("admin_dashboard_complaints exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/admin/dashboard/price_chart', methods=['GET'])
def admin_dashboard_price_chart():
    try:
        if admin_login_session() == 'admin':
            dao = AdminDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_price_chart()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("admin_dashboard_price_chart exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/admin/dashboard/users', methods=['GET'])
def admin_dashboard_users():
    try:
        if admin_login_session() == 'admin':
            dao = AdminDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_all_users()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("admin_dashboard_users exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/admin/dashboard/feedback', methods=['GET'])
def admin_dashboard_feedback():
    try:
        if admin_login_session() == 'admin':
            dao = AdminDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_recent_feedback()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("admin_dashboard_feedback exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


# ── USER DASHBOARD ─────────────────────────────────────────────

@app.route('/user/dashboard', methods=['GET'])
def user_dashboard():
    try:
        if admin_login_session() == 'user':
            return render_template('user/index.html')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_dashboard exception >>>>>>>>>>", ex)


@app.route('/user/dashboard/stats', methods=['GET'])
def user_dashboard_stats():
    try:
        if admin_login_session() == 'user':

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            print(">>>>>>>", login_id)
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_stats(login_id)})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_stats exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/user/dashboard/crop_requests', methods=['GET'])
def user_dashboard_crop_requests():
    try:
        if admin_login_session() == 'user':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_my_crop_requests(login_id)})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_crop_requests exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/user/dashboard/transport_requests', methods=['GET'])
def user_dashboard_transport_requests():
    try:
        if admin_login_session() == 'user':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_my_transport(login_id)})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_transport_requests exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/user/dashboard/bookings', methods=['GET'])
def user_dashboard_bookings():
    try:
        if admin_login_session() == 'user':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_my_bookings(login_id)})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_bookings exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/user/dashboard/complaints', methods=['GET'])
def user_dashboard_complaints():
    try:
        if admin_login_session() == 'user':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_my_complaints(login_id)})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_complaints exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/user/dashboard/price_chart', methods=['GET'])
def user_dashboard_price_chart():
    try:
        if admin_login_session() == 'user':
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_price_chart()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_price_chart exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/user/dashboard/slots', methods=['GET'])
def user_dashboard_slots():
    try:
        if admin_login_session() == 'user':
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_available_slots()})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_slots exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500


@app.route('/user/dashboard/profile', methods=['GET'])
def user_dashboard_profile():
    try:
        if admin_login_session() == 'user':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            dao = UserDashboardDAO()
            return jsonify({'status': 'success', 'data': dao.get_profile(login_id)})
        else:
            return jsonify({'status': 'error'}), 403
    except Exception as ex:
        print("user_dashboard_profile exception >>>>>>>>>>", ex)
        return jsonify({'status': 'error', 'message': str(ex)}), 500