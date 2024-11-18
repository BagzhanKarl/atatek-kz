from datetime import datetime

from atatek.db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)

    country = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(250), nullable=False)

    role = db.Column(db.Integer, default=1, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_verify = db.Column(db.Boolean, nullable=False, default=False)
    is_superadmin = db.Column(db.Boolean, nullable=False, default=False)

    page = db.Column(db.Integer, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Referral(db.Model):
    __tablename__ = 'referrals'

    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Кто пригласил
    referred_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Кто зарегистрировался
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Уникальность пары (referrer_id, referred_id)
    __table_args__ = (db.UniqueConstraint('referrer_id', 'referred_id', name='unique_referral'),)

    # Связь с моделью User
    referrer = db.relationship('User', foreign_keys=[referrer_id], backref=db.backref('referrals_sent', lazy='dynamic'))
    referred = db.relationship('User', foreign_keys=[referred_id], backref=db.backref('referral_received', uselist=False))


class Places(db.Model):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    osm = db.Column(db.String(250), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    display_name = db.Column(db.String(250), nullable=False)