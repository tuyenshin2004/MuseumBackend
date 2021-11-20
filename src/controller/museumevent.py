from datetime import time, date

from flask import request, jsonify
from flask_restful import Resource, reqparse
from models.museumeventDb import Museumevent

from database import ma

class MuseumeventSchema(ma.Schema):
    class Meta:
        fields = ('Description', 'OpenTime', 'CloseTime', 'EventDate', 'Poster')

event_schema = MuseumeventSchema()
events_schema = MuseumeventSchema(many=True)

class Event(Resource):
    def get(self, id):
        evt = Museumevent.find_by_id(id)
        if evt:
            return event_schema.jsonify(evt)
        return {'message': 'Event not found'}, 404

    def post(self, id):
        evt = Museumevent.find_by_id(id)
        if evt:
            return {'message': "An event with name '{}' already exists.".format(id)}, 400

        Description = request.json['Description']
        OpenTime = request.json['OpenTime']
        CloseTime = request.json['CloseTime']
        EventDate = request.json['EventDate']
        Poster = request.json['Poster']
        new_event = Museumevent(Description, OpenTime, CloseTime, EventDate, Poster)
        try:
            new_event.save_to_db()
        except:
            return {"message": "An error occurred inserting the artifact."}, 500
        return {"message": "Event added"}, 201

    def delete(self, id):
        evt = Museumevent.find_by_id(id)
        if evt:
            evt.delete_from_db()
            return {'message': 'Artifact deleted.'}
        return {'message': 'Artifact not found.'}, 404

    def put(self, id):
        evt = Museumevent.find_by_id(id)
        Description = request.json['Description']
        OpenTime = request.json['OpenTime']
        CloseTime = request.json['CloseTime']
        EventDate = request.json['EventDate']
        Poster = request.json['Poster']
        if evt:
            evt.Description = Description
            evt.OpenTime = OpenTime
            evt.CloseTime = CloseTime
            evt.EventDate = EventDate
            evt.Poster = Poster
            evt.save_to_db()
            return event_schema.jsonify(evt)
        return {'message': 'Event not found.'}, 404

class Events(Resource):
    def get(self):
        all_events = Museumevent.query.all()
        result = events_schema.dump(all_events)
        return jsonify(result)

