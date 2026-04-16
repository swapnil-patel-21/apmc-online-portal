import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import *
from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.transportrequest_dao import TransportRequestDAO
from base.com.vo.transportrequest_vo import TransportRequestVO
from base.com.dao.vehicle_dao import VehicleDAO
from base.com.vo.vehicle_vo import VehicleVO
from base.com.dao.login_dao import LoginDAO
from base.com.vo.login_vo import LoginVO
from base.com.dao.croprequest_dao import CropRequestDAO
from base.com.vo.croprequest_vo import CropRequestVO


@app.route('/admin/view_transport_request', methods=['GET'])
def admin_view_transport_request():
    """ Admin view transport request category """
    try:
        if admin_login_session() == 'admin':

            transportrequest_dao = TransportRequestDAO()
            transportrequest_vo_list = transportrequest_dao.admin_view_transportrequest()

            return render_template('admin/viewTransportRequest.html', transportrequest_vo_list=transportrequest_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_transport_request route exception occured>>>>>>>>>>", ex)


@app.route('/user/transport_request', methods=['GET'])
def user_transport_request():
    """ User transport request function """
    try:
        if admin_login_session() == 'user':

            croprequest_dao = CropRequestDAO()
            croprequest_vo = CropRequestVO()
            vehicle_dao = VehicleDAO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_username = request.cookies.get('login_username')
            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)
            croprequest_vo.croprequest_login_id = login_id
            croprequest_vo_list = croprequest_dao.user_view_croprequest(croprequest_vo)
            vehicle_vo_list = vehicle_dao.search_vehicle()

            print(croprequest_vo_list)
            print(vehicle_vo_list)

            return render_template('user/transportRequest.html', vehicle_vo_list=vehicle_vo_list,
                                   croprequest_vo_list=croprequest_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_transport_request route exception occured>>>>>>>>>>", ex)


@app.route('/user/ajax_vehicle', methods=['GET'])
def user_ajax_vehicle():
    """ AJAX call for vehicle list """
    try:
        if admin_login_session() == "user":

            vehicle_vo = VehicleVO()
            vehicle_dao = VehicleDAO()

            vehicle_type = request.args.get('vehicleType')
            print("subcategory_category_id>>>>>>>>>>>>>", vehicle_type)
            vehicle_vo.vehicle_type = vehicle_type
            vehicle_vo_list = vehicle_dao.view_ajax_vehicle(vehicle_vo)
            print("subcategory_vo_list>>>>>", vehicle_vo_list)
            ajax_vehicle = [i.as_dict() for i in vehicle_vo_list]
            print("ajax_product_subcategory>>>>>>>>>>>>>", ajax_vehicle)
            return jsonify(ajax_vehicle)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_ajax_vehicle route exception occured>>>>>>>>>>", ex)

@app.route('/user/insert_transport_request', methods=['GET'])
def user_insert_transport_request():
    """ User insert transport request function """
    try:
        if admin_login_session() == 'user':

            transportrequest_vo = TransportRequestVO()
            transportrequest_dao = TransportRequestDAO()
            vehicle_vo = VehicleVO()
            vehicle_dao = VehicleDAO()
            vehicle_id = request.args.get('vehicleId')
            crop_name_id = request.form.get('cropNameId')
            print(vehicle_id)
            print(crop_name_id)

            vehicle_vo.vehicle_id = vehicle_id
            vehicle_vo_list = vehicle_dao.search_vehicle()
            print(vehicle_vo_list)

            transportrequest_vehicle_type, transportrequest_vehicle_number, transportrequest_vehicle_charge = "", "", ""
            for row in vehicle_vo_list:
                if row.vehicle_id == int(vehicle_id):
                    transportrequest_vehicle_type = row.vehicle_type
                    transportrequest_vehicle_number = row.vehicle_number
                    transportrequest_vehicle_charge = row.vehicle_charge

            login_vo = LoginVO()
            login_dao = LoginDAO()
            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            transportrequest_vo.transportrequest_vehicle_type = transportrequest_vehicle_type
            transportrequest_vo.transportrequest_vehicle_number = transportrequest_vehicle_number
            transportrequest_vo.transportrequest_vehicle_charge = transportrequest_vehicle_charge
            transportrequest_vo.transportrequest_crop_name_id = crop_name_id
            transportrequest_vo.transportrequest_login_id = login_id
            transportrequest_vo.transportrequest_status = "Pending"

            transportrequest_dao.insert_transportrequest(transportrequest_vo)

            return redirect('/user/view_transport_request')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_insert_transport_request route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_transport_request', methods=['GET'])
def user_view_transport_request():
    """ User view transport request category """
    try:
        if admin_login_session() == 'user':

            transportrequest_vo = TransportRequestVO()
            transportrequest_dao = TransportRequestDAO()
            login_vo = LoginVO()
            login_dao = LoginDAO()
            login_username = request.cookies.get('login_username')
            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)
            transportrequest_vo.transportrequest_login_id = login_id
            transportrequest_vo_list = transportrequest_dao.user_view_transportrequest(transportrequest_vo)
            print(transportrequest_vo_list)

            return render_template('user/viewTransportRequest.html', transportrequest_vo_list=transportrequest_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_view_transport_request route exception occured>>>>>>>>>>", ex)


@app.route('/admin/approve_reject_transportrequest', methods=['GET', 'POST'])
def approve_reject_transportrequest():
    try:
        if admin_login_session() == 'admin':

            transportrequest_vo = TransportRequestVO()
            transportrequest_dao = TransportRequestDAO()
            login_dao = LoginDAO()
            login_vo = LoginVO()

            transportrequest_id = request.args.get("transportrequestId")
            transportrequest_vo.transportrequest_id = transportrequest_id
            transportrequest_vo_list = transportrequest_dao.admin_view_transportrequest()
            print(transportrequest_vo_list)

            for row in transportrequest_vo_list:
                if row.transportrequest_id == int(transportrequest_id):
                    login_vo.login_id = row.transportrequest_login_id
                    login_username = login_dao.find_login_username(login_vo)
                    break

            print(login_username)
            sender = os.getenv("EMAIL_USER")
            app_password = os.getenv("EMAIL_PASS")
            receiver = login_username
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver

            status = request.args.get("status")
            if status == "Approve":
                msg_details = "Your Transport Request is Approved"
                transportrequest_vo.transportrequest_status = "Approve"
            elif status == "Reject":
                msg_details = "Your Transport Request is Rejected"
                transportrequest_vo.transportrequest_status = "Reject"

            msg['Subject'] = "APMC Online Portal"
            msg.attach(MIMEText(msg_details, 'plain'))

            server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
            server.starttls()
            server.login(sender, app_password)
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()

            transportrequest_dao.update_croprequest(transportrequest_vo)

            return redirect("/admin/view_transport_request")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("approve_reject_transportrequest route exception occured>>>>>>>>>>", ex)
