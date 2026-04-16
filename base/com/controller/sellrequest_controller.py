import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, redirect, render_template, jsonify

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.crop_dao import CropDAO
from base.com.dao.cropname_dao import CropNameDAO
from base.com.dao.croprequest_dao import CropRequestDAO
from base.com.dao.login_dao import LoginDAO
from base.com.vo.cropname_vo import CropNameVO
from base.com.vo.croprequest_vo import CropRequestVO
from base.com.vo.login_vo import LoginVO


@app.route('/admin/view_sell_request', methods=['GET'])
def admin_view_sell_request():
    try:
        if admin_login_session() == 'admin':
            croprequest_dao = CropRequestDAO()
            croprequest_vo = CropRequestVO()
            croprequest_id = request.args.get("croprequestId")
            croprequest_vo.croprequest_id = croprequest_id
            croprequest_vo_list = croprequest_dao.admin_view_croprequest()
            print(croprequest_vo_list)

            return render_template('admin/viewSellRequest.html', croprequest_vo_list=croprequest_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_sell_request route exception occured>>>>>>>>>>", ex)


@app.route('/admin/approve_reject_request', methods=['GET', 'POST'])
def admin_approve_reject_request():
    try:
        if admin_login_session() == 'admin':

            croprequest_vo = CropRequestVO()
            croprequest_dao = CropRequestDAO()
            login_dao = LoginDAO()
            login_vo = LoginVO()

            croprequest_id = request.args.get("croprequestId")
            croprequest_vo.croprequest_id = croprequest_id
            croprequest_vo_list = croprequest_dao.admin_view_croprequest()
            for row in croprequest_vo_list:
                if row[0].croprequest_id == int(croprequest_id):
                    login_vo.login_id = row[0].croprequest_login_id
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
                msg_details = "Your Crop Sell Request is Approved"
                croprequest_vo.croprequest_status = "Approve"
            elif status == "Reject":
                msg_details = "Your Crop Sell Request is Rejected"
                croprequest_vo.croprequest_status = "Reject"

            msg['Subject'] = "APMC Online Portal"
            msg.attach(MIMEText(msg_details, 'plain'))

            server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
            server.starttls()
            server.login(sender, app_password)
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()

            croprequest_dao.update_croprequest(croprequest_vo)

            return redirect("/admin/view_sell_request")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_approve_reject_request route exception occured>>>>>>>>>>", ex)


@app.route('/user/load_sell_request', methods=['GET'])
def user_load_sell_request():
    """ User sell request function """
    try:
        if admin_login_session() == 'user':

            crop_dao = CropDAO()
            crop_vo_list = crop_dao.search_crop()

            return render_template('user/sellRequest.html', crop_vo_list=crop_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_sell_request route exception occured>>>>>>>>>>", ex)


@app.route('/user/insert_sell_request', methods=['POST'])
def user_insert_sell_request():
    try:
        if admin_login_session() == 'user':

            croprequest_crop_type_id = request.form.get('cropTypeId')
            croprequest_crop_name_id = request.form.get('cropNameId')
            croprequest_crop_quantity = request.form.get('cropRequestQuantity')
            croprequest_crop_description = request.form.get('cropRequestDescription')

            croprequest_vo = CropRequestVO()
            croprequest_dao = CropRequestDAO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            croprequest_vo.croprequest_crop_type = croprequest_crop_type_id
            croprequest_vo.croprequest_crop_name = croprequest_crop_name_id
            croprequest_vo.croprequest_crop_quantity = croprequest_crop_quantity
            croprequest_vo.croprequest_crop_description = croprequest_crop_description
            croprequest_vo.croprequest_login_id = login_id
            croprequest_vo.croprequest_status = "Pending"

            croprequest_dao.insert_croprequest(croprequest_vo)
            return redirect('/user/view_sell_request')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_sell_request route exception occured>>>>>>>>>>", ex)


@app.route('/user/ajax_crop_name', methods=['GET'])
def user_ajax_crop_name():
    try:
        if admin_login_session() == "user":

            cropname_vo = CropNameVO()
            cropname_dao = CropNameDAO()

            crop_type_id = request.args.get('cropTypeId')
            print("subcategory_category_id>>>>>>>>>>>>>", crop_type_id)
            cropname_vo.crop_type_id = crop_type_id
            cropname_vo_list = cropname_dao.view_ajax_cropname(cropname_vo)
            print("subcategory_vo_list>>>>>", cropname_vo_list)
            ajax_cropname = [i.as_dict() for i in cropname_vo_list]
            print("ajax_product_subcategory>>>>>>>>>>>>>", ajax_cropname)
            return jsonify(ajax_cropname)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_ajax_crop_name route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_sell_request', methods=['GET'])
def user_view_sell_request():
    """ User view sell request function """
    try:
        if admin_login_session() == 'user':

            croprequest_vo = CropRequestVO()
            croprequest_dao = CropRequestDAO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_username = request.cookies.get('login_username')
            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)
            croprequest_vo.croprequest_login_id = login_id
            croprequest_vo_list = croprequest_dao.user_view_croprequest(croprequest_vo)

            return render_template('user/viewSellRequest.html', croprequest_vo_list=croprequest_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_view_sell_request route exception occured>>>>>>>>>>", ex)
