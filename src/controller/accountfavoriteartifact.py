from flask_restful import Resource, reqparse
from src.models.accountfavoriteartifactDb import AccountFA

class accountFA(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('AccountId', type=int)
    parser.add_argument('ArtifactId', type=int)

    def get(self, AccId, id):
        acc = AccountFA.find_by_id1(AccId)
        atf = AccountFA.find_by_id2(id)
        if (acc == atf) & (not (acc is None)) :
            return atf.json()
        return {'message': 'ArtifactFavoriteArtifact not found'}, 404

    def post(self):
        data = accountFA.parser.parse_args()
        acc = AccountFA.find_by_id1(data.get('AccountId'))
        atf = AccountFA.find_by_id2(data.get('ArtifactId'))
        if (acc == atf) & (not (acc is None)):
                return {'message': "An ArtifactFavoriteArtifact already exists."}, 400
        art = AccountFA(**data)
        try:
            art.save_to_db()
        except:
            return {"message": "An error occurred inserting the ArtifactFavoriteArtifact."}, 500
        return {"message": "ArtifactFavoriteArtifact added."}, 201

    def delete(self, AccId, id):
        acc = AccountFA.find_by_id1(AccId)
        atf = AccountFA.find_by_id2(id)
        if (acc == atf) & (not (acc is None)):
            acc.delete_from_db()
            return {'message': 'ArtifactFavoriteArtifact deleted.'}
        return {'message': 'ArtifactFavoriteArtifact not found'}, 404

#Hiển thị cả bảng
class accountsFAs(Resource):
    def get(self):
        return {'ArtifactFavoriteArtifacts': list(map(lambda x: x.json(), AccountFA.query.all()))}

#Hiển thị theo typeId
class accountFAs(Resource):
    def get(self, id):
        return {'ArtifactFavoriteArtifacts': list(map(lambda x: x.json(), AccountFA.find_by_id(id)))}

