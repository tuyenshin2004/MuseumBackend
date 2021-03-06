import os

from flask_restful import Resource, reqparse
from src.models.accountDb import AccountDb, RevokedTokenModel
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from src.controller import my_mail
from flask import url_for, jsonify
# from flask_jwt_extended import create_access_token, jwt_required, current_user, get_jwt_identity, get_raw_jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_mail import Message

import json
import re
import random
import string
import jwt
import smtplib
from email.message import EmailMessage
su = URLSafeTimedSerializer('Thisisasecret!') # reformat later


def random_string():
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(6)))
    str1 += ''.join((random.choice(string.digits) for x in range(6)))

    sam_list = list(str1)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


class Account(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)
    parser.add_argument('password', type=str)

    def get(self):
        pass

    def post(self):
        data = Account.parser.parse_args()
        email = data['email']
        password = data['password']
        regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        pattern_mail = re.compile(regex_mail)
        if not pattern_mail.fullmatch(email.lower()) or not password.isalnum():
            return {'message': "Invalid email or password"}, 401
        if AccountDb.find_by_email(email.lower()) is None:
            return {'message': "Incorrect username or password"}, 401
        user = AccountDb.find_by_email(email.lower())
        if check_password_hash(user.Password, password):
            if user.isActivated:
                access_token = create_access_token(identity=email.lower())
                try:
                    return jsonify(access_token=access_token.decode('utf-8'), role=user.RoleId)
                except:
                    return jsonify(access_token=access_token, role=user.RoleId)
            else:
                return {"message": "Please confirm your account via your email"}, 401
        return {"message": "Incorrect username or password"}, 401

    def delete(self):
        return {'message': 'Not allowed'}, 404

    def put(self):
        return {'message': 'Not allowed'}, 404


class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)
    parser.add_argument('password', type=str)

    def get(self):
        pass

    def post(self):
        data = Register.parser.parse_args()
        email = data['email']
        password = data['password']
        regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        pattern_mail = re.compile(regex_mail)
        if not pattern_mail.fullmatch(email.lower()) or not password.isalnum():
            return {'message': "Invalid email or password"}, 400
        if AccountDb.find_by_email(email.lower()) is not None:
            return {'message': "An account with this email already existed."}, 400
        user = AccountDb(email=email.lower(), Password=generate_password_hash(password, method='sha256'),
                         createdAt=datetime.now())
        token = su.dumps(email.lower(), salt='email-confirm')
        link = url_for('confirmation', token=token, _external=False)
        try:
            msg = Message('Confirm Email', sender=os.environ['MAIL'], recipients=[email.lower()])
            msg.body = 'Your link is http://127.0.0.1:5000{}'.format(link)
            my_mail.send(msg)
            user.save_to_db()
        except Exception as e:
            print(e)
            return {'message': "Unable to send confirmation mail"}, 400
        return {'message': "Register success"}, 200

    def delete(self):
        return {'message': 'Not allowed'}, 404

    def put(self):
        return {'message': 'Not allowed'}, 404


class Confirmation(Resource):
    def get(self, token):
        try:
            email = su.loads(token, salt='email-confirm', max_age=3600)
            get_user = AccountDb.find_by_email(email)
            get_user.isActivated = 1
            get_user.confirmedAt = datetime.now()
            get_user.updatedAt = datetime.now()
            get_user.commit_to_db()
        except SignatureExpired:
            return {'message': "The token is expired!"}, 400
        # update email to true
        return {'message': "Activated succeed"}, 200


class Repass(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)

    def post(self):
        data = Repass.parser.parse_args()
        email = data['email']
        regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        pattern_mail = re.compile(regex_mail)
        if not pattern_mail.fullmatch(email.lower()):
            return {'message': "Invalid email"}, 400
        if AccountDb.find_by_email(email.lower()) is None:
            return {'message': "No account with this email"}, 400
        try:
            get_user = AccountDb.find_by_email(email)
            new_password = random_string()
            get_user.Password = generate_password_hash(new_password, method='sha256')
            msg = Message('New Password Recovery', sender=os.environ['MAIL'], recipients=[email.lower()])
            msg.body = 'Your new password is {}'.format(new_password)
            my_mail.send(msg)
            get_user.updatedAt = datetime.now()
            get_user.commit_to_db()
        except:
            return {'message': "Unable to send confirmation mail"}, 400
        return {'message': "New password sent to your mailbox!"}, 200


class ChangePass(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str)
    parser.add_argument('newpassword', type=str)
    parser.add_argument('renewpassword', type=str)

    @jwt_required()
    def post(self):
        data = ChangePass.parser.parse_args()
        password = data['password']
        new_password = data['newpassword']
        re_new_password = data['renewpassword']
        if new_password != re_new_password:
            return {'message': "Not matching new password"}, 400
        email = get_jwt_identity()
        get_user = AccountDb.find_by_email(email)
        if check_password_hash(get_user.Password, password):
            get_user.Password = generate_password_hash(new_password, method='sha256')
            get_user.updatedAt = datetime.now()
            get_user.commit_to_db()
            return {'message': "New password saved succeed!"}, 200
        return {'message': "Wrong password"}, 400


class UserLogoutAccess(Resource):
    """
    User Logout Api
    """

    @jwt_required()
    def post(self):

        # jti = get_raw_jwt()['jti']
        jti = get_jwt()['jti']
        # revoked_token = RevokedTokenModel(jti=jti)
        #
        # revoked_token.add()
        #
        # return {'message': 'Access token has been revoked'}, 200
        try:
            # Revoking access token
            revoked_token = RevokedTokenModel(jti=jti)

            revoked_token.add()

            return {'message': 'Access token has been revoked'}, 200

        except:

            return {'message': 'Something went wrong'}, 500







