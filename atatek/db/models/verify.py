from atatek.db import db
from sqlalchemy.sql import func

class Verify(db.Model):
    __tablename__ = 'verify'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    code = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, server_default=func.now())  # Устанавливаем текущее серверное время
    before_time = db.Column(db.DateTime, server_default=func.now() + func.interval(3, 'minute'))  # Устанавливаем серверное время + 3 минуты
