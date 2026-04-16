from flask import *
from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.vo.timeslot_vo import TimeSlotVO
from base.com.dao.timeslot_dao import TimeSlotDAO


@app.route('/admin/load_timeslot', methods=['GET'])
def admin_load_timeslot():
    """ Admin time slot function """
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/addTimeSlot.html')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_time_slot route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_timeslot', methods=['GET', 'POST'])
def admin_insert_timeslot():
    """ Admin insert time slot function """
    try:
        if admin_login_session() == 'admin':

            timeslot_vo = TimeSlotVO()
            timeslot_dao = TimeSlotDAO()
            timeslot_type = request.form.get("timeslotType")
            timeslot_capacity = request.form.get("timeslotCapacity")

            timeslot_vo.timeslot_type = timeslot_type
            timeslot_vo.timeslot_capacity = timeslot_capacity
            timeslot_dao.insert_timeslot(timeslot_vo)

            return redirect("/admin/view_timeslot")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_insert_timeslot route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_timeslot', methods=['GET'])
def admin_view_timeslot():
    """ Admin view timeslot function """
    try:
        if admin_login_session() == 'admin':

            timeslot_dao = TimeSlotDAO()
            timeslot_vo_list = timeslot_dao.admin_view_timeslot()

            return render_template('admin/viewTimeSlot.html', timeslot_vo_list=timeslot_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_timeslot route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_timeslot', methods=['GET'])
def admin_delete_timeslot():
    """ Admin delete timeslot function """
    try:
        if admin_login_session() == 'admin':

            timeslot_dao = TimeSlotDAO()
            timeslot_vo = TimeSlotVO()

            timeslot_id = request.args.get("timeslotId")
            timeslot_vo.timeslot_id = timeslot_id
            timeslot_dao.delete_timeslot(timeslot_vo)

            return redirect("/admin/view_timeslot")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_timeslot route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_timeslot', methods=['GET'])
def admin_edit_timeslot():
    """ Admin edit timeslot function """
    try:
        if admin_login_session() == 'admin':

            timeslot_dao = TimeSlotDAO()
            timeslot_vo = TimeSlotVO()

            timeslot_id = request.args.get("timeslotId")
            timeslot_vo.timeslot_id = timeslot_id
            timeslot_vo_list = timeslot_dao.edit_timeslot(timeslot_vo)

            return render_template("admin/editTimeslot.html", timeslot_vo_list=timeslot_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_edit_timeslot route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_timeslot', methods=['POST'])
def admin_update_timeslot():
    """ Admin update timeslot function """
    try:
        if admin_login_session() == 'admin':

            timeslot_dao = TimeSlotDAO()
            timeslot_vo = TimeSlotVO()

            timeslot_id = request.form.get("timeslotId")
            timeslot_type = request.form.get("timeslotType")
            timeslot_capacity = request.form.get("timeslotCapacity")

            print(timeslot_id,timeslot_type,timeslot_capacity)

            timeslot_vo.timeslot_id = timeslot_id
            timeslot_vo.timeslot_type = timeslot_type
            timeslot_vo.timeslot_capacity = timeslot_capacity
            timeslot_dao.update_timeslot(timeslot_vo)

            return redirect("/admin/view_timeslot")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_update_timeslot route exception occured>>>>>>>>>>", ex)