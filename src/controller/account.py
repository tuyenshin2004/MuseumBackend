from flask import jsonify
from flask_restful import Resource, reqparse
from src.models.accountDb import Account

class account(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('AccountId', type=str)
    parser.add_argument('displayName', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('Phone', type=str)
    parser.add_argument('Password', type=str)
    parser.add_argument('DOB')
    parser.add_argument('RoleId', type=int)
    parser.add_argument('RecoverPasswordCode', type=str)
    parser.add_argument('ExpiredTimeCode')
    parser.add_argument('FacebookId', type=str)
    parser.add_argument('GoogleId', type=str)
    parser.add_argument('CreateAt')
    parser.add_argument('UpdateAt')
    parser.add_argument('ImageId', type=int)

    def get(self, id):
        acc = Account.find_by_Id(id)
        if acc:
            return acc.json()
        return {'message': 'Event not found'}, 404


    #post put delete phuc lam login

class Accounts(Resource):
    def get(self):
        acc = {'accounts': list(map(lambda x: x.json(), Account.query.all()))}
        return acc
