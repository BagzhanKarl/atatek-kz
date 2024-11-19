# assem/app.py
import json

from flask import Flask, render_template, jsonify, request
from atatek.db import db, Page, Role, Tree
from atatek.endpoints import *
from atatek.endpoints.main import settings_path, token_required
from atatek.utils.get_parent_list import get_list_for_tree

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
@app.route('/uly/<string:bread1>/<string:bread2>/<string:bread3>')
def uly(bread1, bread2, bread3):
    page = db.session.query(Page).filter_by(breed1=bread1, breed2=bread2, breed3=bread3).first()
    res = get_list_for_tree(page.item, db)
    with open(settings_path, 'r') as file:
        settings = json.load(file)

    return render_template('main/index.html', page=page, js='bastay.js', set=settings, start=json.dumps(res))


@app.route('/orta')
def orta():
    return jsonify({"status": True, "data": "Coming soon"})

@app.route('/kishi')
def kishi():
    return jsonify({"status": True, "data": "Coming soon"})

@app.route('/jyzdentys')
def jyzdentys():
    return jsonify({"status": True, "data": "Coming soon"})

@app.route('/qwerty123')
def qwerty123():
    res = get_list_for_tree(25, db)
    return jsonify({"status": True, "data": res})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()