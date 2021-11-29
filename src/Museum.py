from flask_restful import Api
from flask import Flask
from database import db

from controller.images import image, Images
from controller.artifact import artifact, artifacts
from controller.museumevent import Event, Events

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/museum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(image, '/image/<string:name>',  '/image')
api.add_resource(Images, '/images')
api.add_resource(artifact, '/artifact/<string:name>')
api.add_resource(artifacts, '/artifacts')

api.add_resource(Event, '/event/<string:name>')
api.add_resource(Events, '/events')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

