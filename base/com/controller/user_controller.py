import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import *

from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.dao.user_dao import UserDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.user_vo import UserVO


@app.route('/user/register', methods=['GET'])
def user_register():
    """ User Register function """
    try:
        return render_template('user/register.html')
    except Exception as ex:
        print("user_register route exception occured>>>>>>>>>>", ex)


@app.route('/user/submit_register_data', methods=['POST'])
def user_register_submit_data():
    """ User Register Submit Data function """
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()

        user_vo = UserVO()
        user_dao = UserDAO()

        user_firstname = request.form.get('firstName')
        user_lastname = request.form.get('lastName')
        user_gender = request.form.get('gender')
        user_address = request.form.get('address')
        user_contactnumber = request.form.get('contactNumber')
        login_username = request.form.get('userName')

        login_password = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
        print("in user_insert_user login_password>>>>>>>>>", login_password)

        # sender = os.getenv("EMAIL_USER")
        # receiver = login_username
        # msg = MIMEMultipart()
        # msg['From'] = sender
        # msg['To'] = receiver
        # msg['Subject'] = "PYTHON PASSWORD"
        # msg.attach(MIMEText(login_password, 'plain'))

        # server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
        # server.starttls()
        # server.login(sender, "")
        # text = msg.as_string()
        # server.sendmail(sender, receiver, text)
        # server.quit()

        login_secretkey = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(32))
        print("in user_insert_user login_secretkey>>>>>>>", login_secretkey)
        login_vo_list = login_dao.view_login()
        print("in user_insert_user login_vo_list>>>>>>", login_vo_list)
        if len(login_vo_list) != 0:
            for i in login_vo_list:
                if i.login_secretkey == login_secretkey:
                    login_secretkey = ''.join(
                        (random.choice(string.ascii_letters + string.digits)) for x in range(32))
                elif i.login_username == login_username:
                    error_message = "The username is already exists !"
                    flash(error_message)
                    return render_template('user/register.html')

        login_vo.login_username = login_username
        login_vo.login_password = login_password
        login_vo.login_role = "user"
        login_vo.login_status = "active"
        login_vo.login_secretkey = login_secretkey
        login_dao.insert_login(login_vo)

        user_vo.user_firstname = user_firstname
        user_vo.user_lastname = user_lastname
        user_vo.user_gender = user_gender
        user_vo.user_address = user_address
        user_vo.user_contactnumber = user_contactnumber
        user_vo.user_login_id = login_vo.login_id
        user_dao.insert_user(user_vo)

        return render_template('admin/login.html')
    except Exception as ex:
        print("user_register_submit_data route exception occured>>>>>>>>>>", ex)