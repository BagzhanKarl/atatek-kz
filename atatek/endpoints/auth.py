from flask import Blueprint, render_template, request, redirect, make_response
from flask_restx import Api, Resource
from atatek.db import User, db, Page
from atatek.db.models.users import Referral
from atatek.utils import hash_password, check_password, generate_jwt, get_data

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    elif request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']

        user = db.session.query(User).filter_by(phone=phone).first()
        if user and check_password(password, user.password):
            page = db.session.query(Page).filter_by(id=user.page).first()
            token = generate_jwt(user.id, user.first_name, user.last_name, user.role, page=page.title)
            response = make_response(redirect('/'))
            response.set_cookie('token', token)
            return response

        else:
            return render_template('auth/login.html', errorText='Номер телефоныңыз немесе құпиясөз қате')


@auth_bp.route('/auth/logout', methods=['GET', 'POST'])
def logout():
    res = make_response(redirect('/auth/login'))
    res.set_cookie('token', 'bar', max_age=0)
    return res


@auth_bp.route('/auth/register/step1/', defaults={'id': None}, methods=['GET'])
@auth_bp.route('/auth/register/step1/<int:id>', methods=['GET'])
def register_step1(id):
    return render_template('auth/register.html', id=id)



@auth_bp.route('/auth/register/step2/', defaults={'id': None}, methods=['POST'])
@auth_bp.route('/auth/register/step2/<int:id>', methods=['POST'])
def register_step2(id):
    phone = request.form['phone']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template('auth/step2.html', id=id, phone=phone, password=password, first_name=first_name, last_name=last_name)


@auth_bp.route('/auth/register/step3/', defaults={'id': None}, methods=['POST'])
@auth_bp.route('/auth/register/step3/<int:id>', methods=['POST'])
def register_step3(id):
    pages = Page.query.all()
    phone = request.form['phone']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    country = request.form['country']
    osm = request.form['osm']

    return render_template('auth/step3.html', id=id, phone=phone, password=password, first_name=first_name, last_name=last_name, country=country, osm=osm, pages=pages)

@auth_bp.route('/auth/register/step4/', defaults={'id': None}, methods=['POST'])
@auth_bp.route('/auth/register/step4/<int:id>', methods=['POST'])
def register_step4(id):
    phone = request.form['phone']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    country = request.form['country']
    osm = request.form['osm']
    page = request.form['page']

    existing_user = db.session.query(User).filter(User.phone == phone).first()
    if existing_user:
        return redirect('/')

    user = User(
        phone=phone,
        first_name=first_name,
        last_name=last_name,
        country=country,
        address=osm,
        page=page,
        password=hash_password(password),
    )
    db.session.add(user)
    db.session.commit()
    if id is not None:
        referal = Referral(
            referrer_id=id,
            referred_id=user.id,
        )
        db.session.add(referal)
        db.session.commit()
    return redirect('/')

@auth_bp.route('/auth/register/get_place/', methods=['POST'])
def get_place_list():
    country = request.form['country']
    query = request.form['query']
    data = get_data(query, country)
    return data