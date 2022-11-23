from flask import Blueprint, request, render_template
import bcrypt
from database import database
import json
from database.database import get_one_user, get_one_shopping_cart
import  database.database as db
# from database import db
salt = bcrypt.gensalt()
register = Blueprint('register', __name__)


# listing_collection = db['listing']


@register.route('/register', methods=['GET','POST'])
def reg():
    if request.method == "GET":
        return render_template('register_account.html')
    else:
        # after submit form, store the value into database
        # use the lab for id to find the part
        email = request.form.get("email")
        password = bcrypt.hashpw(request.form.get("psw").encode('utf-8'), salt)
        name = request.form.get("name")
        print(f'reg_info being called')
        print(request)
        print(f'username would be {name}')
        print(f'password would be {password}')
        database.create_user_account(email, password, name)


# after submit form, store the value into database
# @register.route('/registration', methods=['POST'])
# def reg_info():
#     # after submit form, store the value into database
#     # use the lab for id to find the part
#     username = request.form.get("uname")
#     password = request.form.get("psw")
#     print(f'reg_info being called')
#     print(request)
#     print(f'username would be {username}')
#     print(f'password would be {password}')
#
#     # # store username and password into database
#     # email = 'hh@gmail.com>>'
#     # db.create_user_account(email, password.encode(), username)
#     #
#     # # print result
#     # res = db.get_one_user('hh@gmail.com>>', password.encode())
#     # print(res)


