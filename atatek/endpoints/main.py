import json
from functools import wraps
from flask import Blueprint, render_template, request, redirect, make_response, url_for

from atatek.db import Role, db, Tree
from atatek.utils import verify_jwt
import os
print(os.getcwd())

settings_path = os.path.join(os.path.dirname(__file__), '../utils/settings.json')
main_bp = Blueprint('Main', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            response = make_response(redirect('/auth/login'))
            return response
        payload = verify_jwt(token)
        if(payload):
            request.user_id = payload['user_id']
            request.first_name = payload['first_name']
            request.last_name = payload['last_name']
            request.role = payload['role']
            request.page = payload['page']
        else:
            response = make_response(redirect('/auth/login'))
            return response
        return f(*args, **kwargs)
    return decorated


@main_bp.route('/')
@token_required
def mainpage():
    with open(settings_path, 'r') as file:
        settings = json.load(file)
    page = request.page
    role = request.role
    jsfile = db.session.query(Role).filter_by(id=role).first()
    start = db.session.query(Tree).filter_by(id=1).first()
    startList = []
    startList.append({
        "id": start.id,
        "name": start.name,
        "gender": 'M',
        "status": 'notmy',
        "born": None,
        "death": None,
        "info": "have"
    })
    return render_template('main/index.html', page=page, js=jsfile.js, set=settings, start=json.dumps(startList))


@main_bp.route('/test')
def testpage():
    role = Role(
        title='Администратор',
        js='admin.js',
        add_child=10,
        add_info=10,

    )
    db.session.add(role)
    db.session.commit()
    return 'Hopa'