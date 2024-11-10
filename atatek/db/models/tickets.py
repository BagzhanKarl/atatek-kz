from datetime import datetime
from atatek.db import db

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer, nullable=False)