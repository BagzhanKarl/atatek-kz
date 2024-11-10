from atatek.db import db


class Config(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    male_badge_background = db.Column(db.String(255))
    male_badge_text = db.Column(db.String(255))
    person_node_background = db.Column(db.String(255))
    person_text = db.Column(db.String(255))
    civilian_border = db.Column(db.String(255))
    person_border = db.Column(db.String(255))

    main_font_style = db.Column(db.String(255))
    main_font_size = db.Column(db.Integer)

    date_font_style = db.Column(db.String(255))
    date_font_size = db.Column(db.Integer)

    bage_font_style = db.Column(db.String(255))
    bage_font_size = db.Column(db.Integer)

    stroke = db.Column(db.Integer)
    radius = db.Column(db.Integer)
    nodespace = db.Column(db.Integer)
    layerspace = db.Column(db.Integer)
    node_x = db.Column(db.Integer)
    node_y = db.Column(db.Integer)
    text_x = db.Column(db.Integer)
    text_y = db.Column(db.Integer)
    text_top = db.Column(db.Float)
    date_top = db.Column(db.Float)

