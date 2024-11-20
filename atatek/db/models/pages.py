from atatek.db import db
from datetime import datetime

class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(255))
    juz = db.Column(db.String(255))
    breed1 = db.Column(db.String(255))
    breed2 = db.Column(db.String(255))
    breed3 = db.Column(db.String(255))
    item = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class Moderator(db.Model):
    __tablename__ = 'moderators'

    id = db.Column(db.Integer, primary_key=True, index=True)
    page = db.Column(db.Integer, db.ForeignKey('pages.id'), nullable=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
