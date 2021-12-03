from src.database import db


class Ticket(db.Model):
    __tablename__ = 'orders'
    OrderId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderDate = db.Column(db.Date)
    TotalPrice = db.Column(db.Integer)
    CreatedAt = db.Column(db.Date)
    QRCode = db.Column(db.String)

    def __init__(self, OrderId, OrderDate, TotalPrice, CreatedAt, QRCode):
        self.OrderId = OrderId
        self.OrderDate = OrderDate
        self.TotalPrice = TotalPrice
        self.CreatedAt = CreatedAt
        self.QRCode = QRCode

    def json(self):
        return {'OrderId': self.OrderId, 'OrderDate': self.OrderDate, 'TotalPrice': self.TotalPrice,
                'CreatedAt': self.CreatedAt, 'QRCode': self.QRCode}
