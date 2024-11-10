from datetime import datetime, timedelta
from atatek.db import db

class Verify(db.Model):
    __tablename__ = 'verify'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    code = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    before_time = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(minutes=3))
