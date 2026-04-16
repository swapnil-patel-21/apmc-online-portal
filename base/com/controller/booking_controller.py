from flask import *
import datetime
import os
import smtplib
from dotenv import load_dotenv
from base import app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.booking_dao import BookingDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.timeslot_dao import TimeSlotDAO
from base.com.dao.croprequest_dao import CropRequestDAO
from base.com.vo.booking_vo import BookingVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.timeslot_vo import TimeSlotVO
from base.com.vo.croprequest_vo import CropRequestVO


@app.route('/user/load_book_slot', methods=['GET'])
def user_book_slot():
    """ User book slot function """
    try:
        if admin_login_session() == 'user':

            timeslot_dao = TimeSlotDAO()
            timeslot_vo = TimeSlotVO()
            croprequest_dao = CropRequestDAO()
            croprequest_vo = CropRequestVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            croprequest_vo.croprequest_login_id = login_id
            croprequest_vo_list = croprequest_dao.user_view_croprequest(croprequest_vo)
            print(croprequest_vo_list)

            date_time = datetime.datetime.now()
            current_date = datetime.date(date_time.year, date_time.month, date_time.day)
            print(current_date)

            timeslot_vo_list = timeslot_dao.user_view_timeslot()
            print(timeslot_vo_list)

            # for value in timeslot_vo_list:
            #     if current_date != value.timeslot_date:
            #         print("Hello")
            #         timeslot_dict = {0:["10:00 to 11:00", 10], 1:["11:00 to 12:00", 10], 2:["12:00 to 13:00", 10]}
            #         for i in range(len(timeslot_dict)):
            #             timeslot_vo.timeslot_type = timeslot_dict[i][0]
            #             timeslot_vo.timeslot_capacity = timeslot_dict[i][1]
            #             print(timeslot_vo.timeslot_type, timeslot_vo.timeslot_capacity)
            #             abc = timeslot_dao.insert_timeslot(timeslot_vo)
            #             print(abc)
            #         break

            return render_template('user/bookingSlot.html', timeslot_vo_list=timeslot_vo_list,
                                   croprequest_vo_list=croprequest_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_book_slot route exception occured>>>>>>>>>>", ex)


@app.route('/user/insert_book_slot', methods=['POST'])
def user_insert_book_slot():
    try:
        if admin_login_session() == 'user':

            booking_vo = BookingVO()
            booking_dao = BookingDAO()
            login_vo = LoginVO()
            login_dao = LoginDAO()
            timeslot_vo = TimeSlotVO()
            timeslot_dao = TimeSlotDAO()

            booking_name_id = request.form.get("bookingNameId")
            booking_date = request.form.get("bookingDate")
            booking_slot_id = request.form.get("bookingSlot")
            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            booking_vo.booking_name_id = booking_name_id
            booking_vo.booking_date = booking_date
            booking_vo.booking_login_id = login_id
            booking_vo.booking_timeslot_id = booking_slot_id
            booking_vo.booking_status = "Pending"

            booking_dao.insert_booking_slot(booking_vo)

            timeslot_vo.timeslot_id = booking_slot_id
            timeslot_vo_list = timeslot_dao.edit_timeslot(timeslot_vo)
            timeslot_capacity = timeslot_vo_list[0].timeslot_capacity
            update_timeslot_capacity = timeslot_capacity - 1

            timeslot_vo.timeslot_capacity = update_timeslot_capacity
            timeslot_dao.update_timeslot(timeslot_vo)

            return redirect('/user/view_booking_request')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_insert_book_slot route exception occured>>>>>>>>>>", ex)


@app.route('/user/ajax_booking_date', methods=['GET'])
def user_ajax_booking_date():
    try:
        if admin_login_session() == "user":

            booking_vo = BookingVO()
            booking_dao = BookingDAO()
            timeslot_dao = TimeSlotDAO()
            timeslot_vo = TimeSlotVO()

            booking_date = request.args.get('bookingDate')
            booking_slot = request.args.get('bookingSlot')

            booking_vo.booking_date = booking_date
            booking_vo.booking_timeslot_id = booking_slot

            booking_vo_list = booking_dao.ajax_view_booking_slot(booking_vo)
            len_booking_vo_list = len(booking_vo_list)

            timeslot_vo.timeslot_id = booking_slot
            timeslot_vo_list = timeslot_dao.edit_timeslot(timeslot_vo)
            timeslot_capacity = timeslot_vo_list[0].timeslot_capacity

            if timeslot_capacity > len_booking_vo_list:
                response = 'Slot is Available!'
                return jsonify({"response": response, "status": True})
            else:
                response = 'Slot is Unavailable!'
                return jsonify({"response": response, "status": False})
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_ajax_booking_date route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_booking_request', methods=['GET'])
def admin_view_book_request():
    """ Admin view book slot function """
    try:
        if admin_login_session() == 'admin':

            booking_dao = BookingDAO()
            booking_vo_list = booking_dao.admin_view_booking_slot()
            print(booking_vo_list)

            return render_template('admin/viewBookingRequest.html', booking_vo_list=booking_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_book_slot route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_booking_request', methods=['GET'])
def user_view_book_request():
    """ User view book slot function """
    try:
        if admin_login_session() == 'user':

            booking_dao = BookingDAO()
            booking_vo = BookingVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            booking_vo.booking_login_id = login_id
            booking_vo_list = booking_dao.user_view_booking_slot(booking_vo)
            print(booking_vo_list)

            return render_template('user/viewBookingRequest.html', booking_vo_list=booking_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_view_book_slot route exception occured>>>>>>>>>>", ex)


@app.route('/admin/approve_reject_book_request', methods=['GET', 'POST'])
def admin_approve_reject_book_request():
    try:
        if admin_login_session() == 'admin':

            booking_vo = BookingVO()
            booking_dao = BookingDAO()
            login_dao = LoginDAO()
            login_vo = LoginVO()
            timeslot_dao = TimeSlotDAO()
            timeslot_vo = TimeSlotVO()

            booking_id = request.args.get("bookId")
            booking_vo.booking_id = booking_id
            book_vo_list = booking_dao.admin_view_booking_slot()
            for row in book_vo_list:
                if row[0].booking_id == int(booking_id):
                    timeslot_vo.timeslot_id = row[1].timeslot_id
                    login_vo.login_id = row[0].booking_login_id
                    login_username = login_dao.find_login_username(login_vo)
                    break

            sender = os.getenv("EMAIL_USER")
            app_password = os.getenv("EMAIL_PASS")
            receiver = login_username
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver

            status = request.args.get("status")
            if status == "Approve":
                msg_details = "Your Booking Request is Approved"
                booking_vo.booking_status = "Approve"
            elif status == "Reject":
                msg_details = "Your Booking Request is Rejected"
                booking_vo.booking_status = "Reject"
                timeslot_vo_list = timeslot_dao.edit_timeslot(timeslot_vo)
                update_timeslot_capacity = (timeslot_vo_list[0].timeslot_capacity) + 1
                timeslot_vo.timeslot_capacity = update_timeslot_capacity
                timeslot_dao.update_timeslot(timeslot_vo)

            msg['Subject'] = "APMC Online Portal"
            msg.attach(MIMEText(msg_details, 'plain'))

            server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
            server.starttls()
            server.login(sender, app_password)
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()

            booking_dao.update_booking(booking_vo)

            return redirect("/admin/view_booking_request")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_approve_reject_request route exception occured>>>>>>>>>>", ex)
