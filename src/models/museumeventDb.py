from sqlalchemy.orm import relationship
import json
import datetime
from database import db


class Museumevent(db.Model):
        __tablename__ = 'museumevent'
        EventId = db.Column(db.Integer, primary_key=True)
        Description = db.Column(db.String(500))
        OpenTime = db.Column(db.Time)
        CloseTime = db.Column(db.Time)
        EventDate = db.Column(db.Date)
        Poster = db.Column(db.Integer, db.ForeignKey('image.ImageId'))
        Image = relationship("Image", foreign_keys=[Poster])

        def __init__(self, Description, OpenTime, CloseTime, EventDate, Poster):
                self.Description = Description
                self.OpenTime = OpenTime
                self.CloseTime = CloseTime
                self.EventDate = EventDate
                self.Poster = Poster



        def json(self):
            return {'Description': self.Description, 'OpenTime': json.dumps(self.OpenTime), 'CloseTime': json.dumps(self.CloseTime),
                    'EventDate': json.dumps(self.EventDate), 'Poster': self.Poster}

        @classmethod
        def find_by_name(cls, name):
            return cls.query.filter_by(Name=name).first()

        @classmethod
        def find_by_id(cls, id):
            return cls.query.filter_by(EventId=id).first()

        def save_to_db(self):
            db.session.add(self)
            db.session.commit()

        def delete_from_db(self):
            db.session.delete(self)
            db.session.commit()