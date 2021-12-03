from src.database import db


class Ticket(db.Model):
    __tablename__ = 'entryticket'
    TicketId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderId = db.Column(db.Integer, db.ForeignKey('orders.OrderId'))
    TicketDate = db.Column(db.Date)
    TimeFrameId = db.Column(db.Integer, db.ForeignKey('timeframe.TimeFrameId'))
    NumberPerson = db.Column(db.Integer)
    TicketType = db.Column(db.Integer, db.ForeignKey('agegroup.GroupId'))

    def __init__(self, TicketId, OrderId, TiketDate, TimeFrameId, NumberPerson, TicketType):
        self.TicketId = TicketId
        self.OrderId = OrderId
        self.TicketDate = TiketDate
        self.TimeFrameId = TimeFrameId
        self.NumberPerson = NumberPerson
        self.TicketType = TicketType

    def json(self):
        return {'TicketId': self.TicketId, 'OrderId': self.OrderId, 'TiketDate': self.TicketDate,
                'TimeFrameId':  self.TimeFrameId, 'NumberPerson': self.NumberPerson, 'TicketType': self.TicketType}


