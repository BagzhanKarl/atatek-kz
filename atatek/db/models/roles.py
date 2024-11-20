from atatek.db import db

class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    js = db.Column(db.String(80), unique=True, nullable=False)
    add_child = db.Column(db.Integer, nullable=False, default=False)
    add_info = db.Column(db.Integer, nullable=False, default=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f'<Role {self.id}>'
