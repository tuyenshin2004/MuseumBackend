from flask_restful import Api
from flask import Flask
from database import db

from controller.images import image, Images
from controller.artifact import artifact, artifacts
from controller.museumevent import Event, Events
from controller.souvenir import souvenir, souvenirs
from controller.artifacttype import artifactType, artifactTypes
from controller.account import account, Accounts
from controller.artifacttypemapping import artifactTypeMapping, artifactTypeMappings, artifactsType
from controller.accountfavoriteartifact import accountFA, accountFAs,accountsFAs
from controller.rattings import Rattings, ratting
from controller.notification import notification, Notifications

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/museum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(image, '/image/<string:name>',  '/image')
api.add_resource(Images, '/images')
api.add_resource(artifact, '/artifact/<string:name>')
api.add_resource(artifacts, '/artifacts')

api.add_resource(Event, '/event/<string:name>', '/event')
api.add_resource(Events, '/events')

api.add_resource(souvenir, '/souvenir/<string:name>', '/souvenir')
api.add_resource(souvenirs, '/souvenirs')

api.add_resource(artifactType, '/artifactType/<string:name>', '/artifactType')
api.add_resource(artifactTypes, '/artifactTypes')

api.add_resource(account, '/account/<int:id>')
api.add_resource(Accounts, '/accounts')

api.add_resource(Rattings, '/rattings')
api.add_resource(ratting, '/ratting/<int:id>', '/ratting')

api.add_resource(Notifications, '/notifications')
api.add_resource(notification, '/notification/<int:id>')

api.add_resource(artifactTypeMapping, '/artifactTypeMapping/<int:id>&<int:typeId>', '/artifactTypeMapping')
api.add_resource(artifactTypeMappings, '/artifactTypeMappings')
api.add_resource(artifactsType, '/artifactsType/<int:id>')

#accountFavoriteArtifact
api.add_resource(accountFA, '/accountFA/<int:AccId>&<int:id>', '/accountFA')
api.add_resource(accountsFAs, '/accountFAs')
api.add_resource(accountFAs, '/accountFAs/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

