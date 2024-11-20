from atatek.db import db
from datetime import datetime

class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, index=True)
    page = db.Column(db.Integer, db.ForeignKey('pages.id'))

    title = db.Column(db.String(255))
    poster = db.Column(db.String(255))
    content = db.Column(db.Text)

    # Использование функции NOW() для времени создания и обновления
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
