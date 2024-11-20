from atatek.db import db

class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    role = db.Column(db.Integer)
    childCount = db.Column(db.Integer)
    infoCount = db.Column(db.Integer)

    # Добавляем время создания и обновления
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
