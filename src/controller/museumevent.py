from datetime import time, date

from flask import request, jsonify
from flask_restful import Resource, reqparse
from models.museumeventDb import Museumevent

class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Description', type=str)
    parser.add_argument('OpenTime')
    parser.add_argument('CloseTime')
    parser.add_argument('EventDate')
    parser.add_argument('Poster', type=int)

    def get(self, id):
        evt = Museumevent.find_by_id(id)
        if evt:
            return evt.json
        return {'message': 'Event not found'}, 404

    def post(self, id):
        if Museumevent.find_by_id(id):
            return {'message': "An event with name '{}' already exists.".format(id)}, 400
        data = Event.parser.parse_args()
        evt = Museumevent(id, **data)
        try:
            evt.save_to_db()
            return evt.json, 201
        except Exception as e:
            print(e)
            return {"message": "An error occurred inserting the artifact."}, 500


    def delete(self, id):
        evt = Museumevent.find_by_id(id)
        if evt:
            evt.delete_from_db()
            return {'message': 'Artifact deleted.'}
        return {'message': 'Artifact not found.'}, 404

    def put(self, id):
        data = Event.parser.parse_args()
        evt = Museumevent.find_by_id(id)

        if evt:
            evt.id = id
            evt.Description = data['Description']
            evt.OpenTime = data['OpenTime']
            evt.CloseTime = data['CloseTime']
            evt.EventDate = data['EventDate']
            evt.Poster = data['Poster']
            evt.save_to_db()
            return evt.json
        return {'message': 'Event not found.'}, 404

class Events(Resource):
    def get(self):
        evt= {'events': list(map(lambda x: x.json, Museumevent.query.all()))}
        return evt
