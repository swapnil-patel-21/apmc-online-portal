from flask import *

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.crop_dao import CropDAO
from base.com.vo.crop_vo import CropVO
from base.com.dao.cropname_dao import CropNameDAO
from base.com.vo.cropname_vo import CropNameVO


@app.route('/admin/add_crop', methods=['GET'])
def admin_add_crop():
    """ Admin crop insert function """
    try:
        if admin_login_session() == 'admin':
            return render_template("admin/addCrop.html")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_add_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/submit_crop', methods=['POST'])
def admin_submit_crop():
    """ Admin crop submit function """
    try:
        if admin_login_session() == 'admin':
            crop_type = request.form.get('cropType')
            crop_name = request.form.get('cropName')
            crop_description = request.form.get('cropDescription')

            crop_vo = CropVO()
            crop_dao = CropDAO()
            crop_name_vo = CropNameVO()
            crop_name_dao = CropNameDAO()

            crop_vo_list = crop_dao.search_crop()
            crop_type_list = []
            for row in crop_vo_list:
                crop_type_list.append(row.crop_type)

            for row in crop_vo_list:
                if crop_type in crop_type_list:
                    crop_id = row.crop_id
                    crop_vo.crop_id = crop_id
                    break
                else:
                    crop_vo.crop_type = crop_type
                    crop_dao.insert_crop(crop_vo)
                    break
            else:
                crop_vo.crop_type = crop_type
                crop_dao.insert_crop(crop_vo)

            crop_name_vo.crop_name = crop_name
            crop_name_vo.crop_description = crop_description
            crop_name_vo.crop_type_id = crop_vo.crop_id

            crop_name_dao.insert_crop_name(crop_name_vo)
            return redirect('/admin/view_crop')
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_submit_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_crop', methods=['GET'])
def admin_view_crop():
    """ Admin view crop function """
    try:
        if admin_login_session() == 'admin':

            crop_name_dao = CropNameDAO()
            crop_name_vo_list = crop_name_dao.search_crop_name()

            return render_template('admin/viewCrop.html', crop_name_vo_list=crop_name_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_crop', methods=['GET'])
def admin_delete_crop():
    """Admin crop delete function"""
    try:
        if admin_login_session() == 'admin':
            crop_vo = CropVO()
            crop_dao = CropDAO()
            crop_name_vo = CropNameVO()
            crop_name_dao = CropNameDAO()
            crop_id = request.args.get('cropId')
            crop_name_id = request.args.get('cropNameId')
            crop_vo.crop_id = crop_id

            crop_name_vo.crop_name_id = crop_name_id
            crop_name_dao.delete_crop_name(crop_name_vo)

            crop_name_vo_list = crop_name_dao.search_crop_name()
            flag = False
            for row in crop_name_vo_list:
                if row[0].crop_type_id == crop_id:
                    flag = True
                    break

            if flag != True:
                crop_dao.delete_crop(crop_vo)

            return redirect('admin/view_crop')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_crop', methods=['GET'])
def admin_edit_crop():
    """ Admin crop edit function """
    try:
        if admin_login_session() == 'admin':

            crop_vo = CropVO()
            crop_dao = CropDAO()
            crop_name_dao = CropNameDAO()
            crop_name_vo = CropNameVO()
            crop_id = request.args.get('cropId')
            crop_name_id = request.args.get('cropNameId')
            crop_vo.crop_id = crop_id
            crop_vo_list = crop_dao.edit_crop(crop_vo)

            crop_name_vo.crop_name_id = crop_name_id
            crop_name_vo_list = crop_name_dao.edit_crop_name(crop_name_vo)

            return render_template('admin/editCrop.html', crop_vo_list=crop_vo_list, crop_name_vo_list=crop_name_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_edit_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_crop', methods=['GET', 'POST'])
def admin_update_crop():
    """ Admmin crop update function """
    try:
        if admin_login_session() == 'admin':

            crop_type = request.form.get('cropType')
            crop_name = request.form.get('cropName')
            crop_description = request.form.get('cropDescription')
            crop_name_id = request.form.get('cropNameId')

            crop_vo = CropVO()
            crop_dao = CropDAO()
            crop_name_dao = CropNameDAO()
            crop_name_vo = CropNameVO()

            crop_vo.crop_type = crop_type
            crop_vo_list = crop_dao.search_crop()
            crop_type_list = []
            for row in crop_vo_list:
                crop_type_list.append(row.crop_type)

            for row in crop_vo_list:
                if crop_type in crop_type_list:
                    if row.crop_type == crop_type:
                        crop_type_id = row.crop_id
                else:
                    crop_dao.insert_crop(crop_vo)

            crop_vo.crop_type = crop_type
            crop_vo_list = crop_dao.search_crop()
            for row in crop_vo_list:
                if row.crop_type == crop_type:
                    crop_type_id = row.crop_id

            crop_name_vo.crop_name_id = crop_name_id
            crop_name_vo.crop_name = crop_name
            crop_name_vo.crop_description = crop_description
            crop_name_vo.crop_type_id = crop_type_id

            crop_name_dao.update_crop_name(crop_name_vo)

            return redirect('/admin/view_crop')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_update_crop route exception occured>>>>>>>>>>", ex)
