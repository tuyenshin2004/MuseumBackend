import datetime

from sqlalchemy.orm import relationship

from src.database import db

class Account(db.Model):
    __tablename__ = 'account'
    AccountId = db.Column(db.Integer, primary_key=True)
    displayName = db.Column(db.String(100))
    email = db.Column(db.String(50))
    Phone = db.Column(db.String(50))
    Password = db.Column(db.String(50))
    DOB = db.Column(db.Date)
    RoleId = db.Column(db.Integer)
    RecoverPasswordCode = db.Column(db.String(50))
    ExpiredTimeCode = db.Column(db.Date)
    FacebookId = db.Column(db.String(50))
    GoogleId = db.Column(db.String(50))
    CreateAt = db.Column(db.Date)
    UpdateAt = db.Column(db.Date)
    ImageId = db.Column(db.Integer, db.ForeignKey('image.ImageId'))
    Image = relationship("Image", foreign_keys=[ImageId])

    def __init__(self, AccountId, displayName, email, Phone, Password, DOB, RoleId, RecoverPasswordCode, ExpiredTimeCode, FacebookId, GoogleId, CreateAt, UpdateAt,ImageId ):
        self.AccountId = AccountId
        self.displayName = displayName
        self.email = email
        self.Phone = Phone
        self.Password = Password
        self.DOB = DOB
        self.RoleId = RoleId
        self.RoleId = RoleId
        self.RecoverPasswordCode = RecoverPasswordCode
        self.ExpiredTimeCode =ExpiredTimeCode
        self.FacebookId = FacebookId
        self.GoogleId = GoogleId
        self.CreateAt = CreateAt
        self.UpdateAt = UpdateAt
        self.ImageId = ImageId

    def json(self):
        if isinstance(self.DOB, datetime.date):
            self.DOB = self.DOB.strftime("%Y-%m-%d")

        if isinstance(self.ExpiredTimeCode, datetime.date):
            self.ExpiredTimeCode = self.ExpiredTimeCode.strftime("%Y-%m-%d")

        if isinstance(self.CreateAt, datetime.date):
            self.CreateAt = self.CreateAt.strftime("%Y-%m-%d")

        if isinstance(self.UpdateAt, datetime.date):
            self.UpdateAt = self.UpdateAt.strftime("%Y-%m-%d")

        return {"AccountId": self.AccountId, "displayName": self.displayName, "email": self.email, "Phone": self.Phone, "Password": self.Password, "DOB": self.DOB, "RoleId": self.RoleId, "RecoverPasswordCode": self.RecoverPasswordCode,
                "ExpiredTimeCode":self.ExpiredTimeCode, "FacebookId": self.FacebookId, "GoogleId": self.GoogleId, "CreateAt": self.CreateAt, "UpdateAt": self.UpdateAt, "ImageId": self.ImageId}

    @classmethod
    def find_by_Id(cls, id):
        return cls.query.filter_by(AccountId = id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()