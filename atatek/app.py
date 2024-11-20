from flask import Flask
from atatek.db import db
from atatek.endpoints import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/atatek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TIMEZONE'] = 'UTC'  # или 'Asia/Almaty'

db.init_app(app)  # Инициализация базы данных с приложением

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)
app.register_blueprint(profile)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(tests, url_prefix='/admin/admin')
app.register_blueprint(ulyjyz)



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()