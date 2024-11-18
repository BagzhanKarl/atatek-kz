# assem/app.py
from flask import Flask, render_template, jsonify
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
app.register_blueprint(profile)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(tests, url_prefix='/admin/admin')


@app.route('/landing')
def landing():
    return jsonify({"status": True, "data": "Coming soon"})
@app.route('/uly')
def uly():
    return jsonify({"status": True, "data": "Coming soon"})

@app.route('/orta')
def orta():
    return jsonify({"status": True, "data": "Coming soon"})

@app.route('/kishi')
def kishi():
    return jsonify({"status": True, "data": "Coming soon"})

@app.route('/jyzdentys')
def jyzdentys():
    return jsonify({"status": True, "data": "Coming soon"})

with app.app_context():
    db.create_all()
