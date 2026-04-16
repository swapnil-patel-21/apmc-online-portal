from flask import *
import datetime

from base import app
from base.com.dao.cropname_dao import CropNameDAO
from base.com.dao.crop_dao import CropDAO
from base.com.dao.pricechart_dao import PriceChartDAO
from base.com.vo.pricechart_vo import PriceChartVO
from base.com.controller.login_controller import admin_login_session, admin_logout_session


@app.route('/admin/add_price', methods=['GET'])
def admin_add_price():
    """ Admin add price function """
    try:
        crop_name_dao = CropNameDAO()
        crop_name_vo_list = crop_name_dao.search_crop_name()

        local_date_time = datetime.datetime.now()
        local_year = local_date_time.year
        local_month = local_date_time.month
        local_day = local_date_time.day

        price_chart_dao = PriceChartDAO()
        price_chart_vo_list = price_chart_dao.admin_view_price()
        temp_list = []

        for value in price_chart_vo_list:
            crop_price_date = (value[0].crop_price_date)
            crop_price_date_time_day = crop_price_date.day
            crop_price_date_time_month = crop_price_date.month
            crop_price_date_time_year = crop_price_date.year

            if local_year == crop_price_date_time_year and local_month == crop_price_date_time_month \
                    and local_day == crop_price_date_time_day:
                temp_list.append(value)

        for raw in temp_list:
            for value in crop_name_vo_list:
                if raw[1] == value[0]:
                    crop_name_vo_list.pop(crop_name_vo_list.index(value))


        return render_template('admin/addPrice.html', crop_name_vo_list=crop_name_vo_list)
    except Exception as ex:
        print("admin_add_price route exception occured>>>>>>>>>>", ex)


@app.route('/admin/submit_add_price', methods=['POST'])
def admin_submit_add_price():
    """ Admin submit add price function """
    try:
        if admin_login_session() == 'admin':
            price_chart_crop_id = request.form.get('priceChartCropId')
            crop_price = request.form.get('cropPrice')

            print(price_chart_crop_id, crop_price)

            local_date_time = datetime.datetime.now()
            local_year = local_date_time.year
            local_month = local_date_time.month
            local_day = local_date_time.day
            crop_price_date = datetime.date(local_year, local_month, local_day)

            price_chart_vo = PriceChartVO()
            price_chart_dao = PriceChartDAO()

            price_chart_vo.price_chart_crop_id = price_chart_crop_id
            price_chart_vo.crop_price = crop_price
            price_chart_vo.crop_price_date = crop_price_date
            price_chart_dao.insert_price(price_chart_vo)

            print("Done")

            return redirect('admin/view_price')
        else:
            print("Not admin role")
    except Exception as ex:
        print("admin_submit_add_price route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_price', methods=['GET'])
def admin_view_price():
    """ Admin view price function """
    try:
        if admin_login_session() == 'admin':
            price_chart_dao = PriceChartDAO()
            price_chart_vo_list = price_chart_dao.admin_view_price()
            print(price_chart_vo_list)
            return render_template('admin/viewPrice.html', price_chart_vo_list=price_chart_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_price route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_price', methods=['GET'])
def admin_delete_price():
    """Admin delete price function"""
    try:
        if admin_login_session() == 'admin':
            price_chart_vo = PriceChartVO()
            price_chart_dao = PriceChartDAO()
            price_chart_id = request.args.get('priceChartId')
            price_chart_vo.price_chart_id = price_chart_id
            price_chart_dao.delete_price(price_chart_vo)
            return redirect('admin/view_price')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_price route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_price', methods=['GET'])
def admin_edit_price():
    """Admin edit price function"""
    try:
        if admin_login_session() == 'admin':
            price_chart_vo = PriceChartVO()
            price_chart_dao = PriceChartDAO()
            crop_dao = CropDAO()

            price_chart_id = request.args.get('priceChartId')
            price_chart_vo.price_chart_id = price_chart_id
            price_chart_vo_list = price_chart_dao.edit_price(price_chart_vo)
            print(price_chart_vo_list)

            return render_template('admin/editPrice.html', price_chart_vo_list=price_chart_vo_list)
        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_edit_price route exception occured>>>>>>>>>>", ex)


@app.route('/admin/submit_update_price', methods=['POST'])
def admin_update_price():
    """Admin update price function"""
    try:
        if admin_login_session() == 'admin':
            price_chart_id = request.form.get('priceChartId')
            crop_price = request.form.get('cropPrice')
            price_chart_crop_id = request.form.get('priceChartCropId')

            price_chart_vo = PriceChartVO()
            price_chart_dao = PriceChartDAO()

            price_chart_vo.price_chart_id = price_chart_id
            price_chart_vo.crop_price = crop_price
            price_chart_vo.price_chart_crop_id = price_chart_crop_id
            price_chart_dao.update_price(price_chart_vo)
            return redirect('/admin/view_price')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_update_price route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_price_chart', methods=['GET'])
def user_price_chart():
    """ User Display Price function """
    try:
        if admin_login_session() == 'user':

            update_pricechart_vo_list = []
            yesterday_price_dict = {}
            pricechart_dao = PriceChartDAO()
            pricechart_vo_list = pricechart_dao.user_view_price()
            print(pricechart_vo_list)

            current_date = datetime.date.today()
            # print("Today Date:", current_date)
            yesterday_year, yesterday_month, yesterday_date = get_yesterday_date(current_date)
            # print("yesterday Year:", yesterday_year)
            # print("yesterday Month:", yesterday_month)
            # print("Yesterday Date:", yesterday_date)

            yesterday_full_date = datetime.date(yesterday_year, yesterday_month, yesterday_date)
            print("Yesterday Date>>>>>>>>>", yesterday_full_date)

            for value in pricechart_vo_list:
                if current_date == value[0].crop_price_date:
                    update_pricechart_vo_list.append(value)
                if yesterday_full_date == value[0].crop_price_date:
                    yesterday_price_dict[value[0].price_chart_crop_id] = value[0].crop_price

            for row in update_pricechart_vo_list:
                yesterday_price = yesterday_price_dict.get(row[0].price_chart_crop_id)
                if yesterday_price == None:
                    yesterday_price_dict[row[0].price_chart_crop_id] = 0

            print(update_pricechart_vo_list)
            print(yesterday_price_dict)

            return render_template('user/viewPriceChart.html', update_pricechart_vo_list=update_pricechart_vo_list,
                                   yesterday_price_dict=yesterday_price_dict, yesterday_full_date=yesterday_full_date)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_price_chart route exception occured>>>>>>>>>>", ex)


def get_yesterday_date(current_date):
    if current_date.day == 1:

        # Logic for year
        if current_date.month == 1:
            yesterday_year = (current_date.year - 1)
        else:
            yesterday_year = current_date.year

        # Logic for month
        if current_date.month == 1:
            yesterday_month = 12
        else:
            yesterday_month = (current_date.month - 1)

        # Logic for day
        if current_date.month in [3, 5, 7, 10, 12]:
            if current_date.month == 3:
                if current_date.year % 4 == 0:
                    yesterday_date = 29
                else:
                    yesterday_date = 28
            else:
                yesterday_date = 30
        else:
            yesterday_date = 31
    else:
        yesterday_date = (current_date.day - 1)
        yesterday_month = current_date.month
        yesterday_year = current_date.year

    return yesterday_year, yesterday_month, yesterday_date