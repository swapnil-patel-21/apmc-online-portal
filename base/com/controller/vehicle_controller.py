import os

from flask import *
from werkzeug.utils import secure_filename

from base import app
from base.com.dao.vehicle_dao import VehicleDAO
from base.com.vo.vehicle_vo import VehicleVO
from base.com.controller.login_controller import admin_login_session, admin_logout_session

DATASET_FOLDER = 'base/static/adminResources/dataset/'

app.config['DATASET_FOLDER'] = DATASET_FOLDER


@app.route('/admin/add_vehicle', methods=['GET'])
def admin_add_vehicle():
    """ Admin add dataset category """
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/addVehicle.html')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_add_vehicle route exception occured>>>>>>>>>>", ex)


@app.route('/admin/submit_vehicle', methods=['POST'])
def admin_submit_vehicle():
    """ Admin dataset submit function """
    try:
        if admin_login_session() == 'admin':
            vehicle_type = request.form.get('vehicleType')
            vehicle_number = request.form.get('vehicleNumber')
            vehicle_charge = request.form.get('vehicleCharge')
            vehicle_image = request.files.get('vehicleImage')

            vehicle_image_name = secure_filename(vehicle_image.filename)
            vehicle_image_path = os.path.join(app.config['DATASET_FOLDER'])
            vehicle_image.save(os.path.join(vehicle_image_path, vehicle_image_name))

            vehicle_vo = VehicleVO()
            vehicle_dao = VehicleDAO()

            vehicle_vo.vehicle_type = vehicle_type
            vehicle_vo.vehicle_number = vehicle_number
            vehicle_vo.vehicle_charge = vehicle_charge
            vehicle_vo.vehicle_image_name = vehicle_image_name
            vehicle_vo.vehicle_image_path = vehicle_image_path.replace("base", "..")
            vehicle_dao.insert_vehicle(vehicle_vo)
            return redirect('admin/view_vehicle')
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_submit_vehicle route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_vehicle', methods=['GET'])
def admin_view_vehicle():
    """ Admin view dataset category """
    try:
        if admin_login_session() == 'admin':
            vehicle_dao = VehicleDAO()
            vehicle_vo_list = vehicle_dao.search_vehicle()
            return render_template('admin/viewVehicle.html', vehicle_vo_list=vehicle_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_vehicle route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_vehicle', methods=['GET'])
def admin_delete_vehicle():
    """Admin dataset delete function"""
    try:
        if admin_login_session() == 'admin':
            vehicle_vo = VehicleVO()
            vehicle_dao = VehicleDAO()
            vehicle_id = request.args.get('vehicleId')
            print(vehicle_id)
            vehicle_vo.vehicle_id = vehicle_id
            vehicle_vo_list = vehicle_dao.delete_vehicle(vehicle_id)
            file_path = vehicle_vo_list.vehicle_image_path.replace("..", "base") + vehicle_vo_list.vehicle_image_name
            os.remove(file_path)
            return redirect('admin/view_vehicle')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_vehicle route exception occured>>>>>>>>>>", ex)


@app.route('/user/vehicle_chart', methods=['GET'])
def user_vehicle_chart():
    """ User Display Vehicle function """
    try:
        if admin_login_session() == 'user':

            vehicle_dao = VehicleDAO()
            vehicle_vo_list = vehicle_dao.search_vehicle()
            return render_template('user/viewVehicleChart.html', vehicle_vo_list=vehicle_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_view_vehicle route exception occured>>>>>>>>>>", ex)
