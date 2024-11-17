from atatek.db import db

class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    js = db.Column(db.String(80), unique=True, nullable=False)
    add_child = db.Column(db.Integer, nullable=False, default=False)
    add_info = db.Column(db.Integer, nullable=False, default=False)

    def __repr__(self):
        return '<Role %r>' % self.id