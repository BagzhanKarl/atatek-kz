# assem/app.py
from flask import Flask, render_template
from atatek.db import db, Page
from atatek.endpoints import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/atatek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db.init_app(app)  # Инициализация базы данных с приложением

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)


with app.app_context():
    db.create_all()
