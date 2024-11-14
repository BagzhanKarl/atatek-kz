from atatek.db import db

class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    role = db.Column(db.Integer)
    childCount = db.Column(db.Integer)
    infoCount = db.Column(db.Integer)


