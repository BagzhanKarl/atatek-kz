from datetime import datetime
from atatek.db import db

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))

    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_cancelled = db.Column(db.Boolean, nullable=False, default=False)
    is_completed = db.Column(db.Boolean, nullable=False, default=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    #edit
    name = db.Column(db.String(50))
    birth = db.Column(db.String(50))
    death = db.Column(db.String(50))
    info = db.Column(db.Text)
    tree_id = db.Column(db.Integer)

    #add
    name_new = db.Column(db.String(50))
    parent = db.Column(db.Integer)

