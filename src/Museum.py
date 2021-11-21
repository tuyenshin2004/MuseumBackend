from flask_restful import Api
from flask import Flask
from database import db

from controller.images import image, Images
from controller.artifact import artifact, artifacts
from controller.museumevent import Event, Events
from controller.account import Account, Accounts
from controller.rattings import Rattings, ratting
from controller.notification import notification, Notifications

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/museum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api: Api = Api(app)

api.add_resource(image, '/image/<string:name>',  '/image')
api.add_resource(Images, '/images')
api.add_resource(artifact, '/artifact/<string:name>')
api.add_resource(artifacts, '/artifacts')

api.add_resource(Event, '/event/<string:name>')
api.add_resource(Events, '/events')


api.add_resource(Accounts, '/accounts')

api.add_resource(Rattings, '/rattings')
api.add_resource(ratting, '/ratting/<int:id>')

api.add_resource(Notifications, '/notifications')
api.add_resource(notification, '/notification/<int:id>')
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

