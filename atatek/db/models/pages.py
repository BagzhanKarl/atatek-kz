from operator import index

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