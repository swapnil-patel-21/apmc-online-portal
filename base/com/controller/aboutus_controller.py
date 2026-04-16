
from flask import *
from base import app


@app.route('/user/about_us', methods=['GET'])
def user_aboutus():
    """ User About US function """
    try:
        return render_template('user/about.html')
    except Exception as ex:
        print("user_about_us route exception occured>>>>>>>>>>", ex)

