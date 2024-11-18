from datetime import datetime
from atatek.db import db

class Tree(db.Model):
    __tablename__ = 'tree'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.Integer, nullable=True)
    death_year = db.Column(db.Integer, nullable=True)

    parent_id = db.Column(db.Integer, db.ForeignKey('tree.id'))
    juz = db.Column(db.Integer, db.ForeignKey('tree.id'))

    # Устанавливаем связь с родителем
    parent = db.relationship('Tree', remote_side=[id], foreign_keys=[parent_id], backref='children')
    # Устанавливаем связь для поля juz
    juz_item = db.relationship('Tree', remote_side=[id], foreign_keys=[juz], backref='related_juz')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, default=0, nullable=False)
    updated_by = db.Column(db.Integer, default=0, nullable=False)


class TreeInfo(db.Model):
    __tablename__ = 'tree_info'

    id = db.Column(db.Integer, primary_key=True)
    tree_id = db.Column(db.Integer, db.ForeignKey('tree.id'))
    info = db.Column(db.Text, nullable=False)
    tree_icon = db.Column(db.String(100), nullable=True)
    tree_full_icon = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, default=0, nullable=False)
    updated_by = db.Column(db.Integer, default=0, nullable=False)