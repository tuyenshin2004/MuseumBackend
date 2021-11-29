from flask_restful import Api
from flask import Flask
from database import db

from controller.images import image, Images
from controller.artifact import artifact, artifacts
from controller.museumevent import Event, Events
from src.controller.account import Account, Register, Confirmation, Repass, ChangePass, UserLogoutAccess
from src import controller


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/museum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('core/config.py')

api = Api(app)
controller.init_app(app)

api.add_resource(image, '/image/<string:name>',  '/image')
api.add_resource(Images, '/images')
api.add_resource(artifact, '/artifact/<string:name>')
api.add_resource(artifacts, '/artifacts')
api.add_resource(Event, '/event/<string:name>')
api.add_resource(Events, '/events')
api.add_resource(Account, '/login')
api.add_resource(Register, '/register')
api.add_resource(Confirmation, '/confirm_email/<token>')
api.add_resource(Repass, '/repass')
api.add_resource(ChangePass, '/changepass')
api.add_resource(UserLogoutAccess, '/logout')

@controller.jwt_manager.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):

    jti = decrypted_token['jti']

    return controller.account.RevokedTokenModel.is_jti_blacklisted(jti)




if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

