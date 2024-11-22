from flask import Blueprint, render_template, request, redirect

from atatek.db import db, User
from atatek.db import Ticket
from atatek.endpoints.main import token_required
from atatek.utils.get_parent_list import get_list_for_tree

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@token_required
def profile_file():
    user = request.user_id
    userData = User.query.filter_by(id=user).first()
    page = request.page
    tickets = db.session.query(Ticket).filter_by(created_by=user).order_by(Ticket.created_at.desc()).all()
    treelist = get_list_for_tree(25, db)
    return render_template('profile/profile.html', first_name=userData.first_name, last_name=userData.last_name, tickets=tickets, page=page, id=user, treelist=treelist)

@profile.route('/profile/edit', methods=['GET', 'POST'])
@token_required
def profile_edit():
    if request.method == 'POST':
        user_id = request.user_id
        update_user = db.session.query(User).filter_by(id=user_id).first()

        # Проверяем и обновляем только заполненные поля
        if 'first_name' in request.form and request.form['first_name']:
            update_user.first_name = request.form['first_name']

        if 'last_name' in request.form and request.form['last_name']:
            update_user.last_name = request.form['last_name']

        if 'country' in request.form and request.form['country']:
            update_user.country = request.form['country']

        if 'ru' in request.form and request.form['ru']:
            update_user.page = request.form['ru']

        if 'osm' in request.form and request.form['osm']:
            update_user.address = request.form['osm']

        # Сохраняем изменения, если что-то было изменено
        db.session.commit()

        return redirect('/profile')

    else:
        user = request.user_id
        page = request.page
        userform = db.session.query(User).filter_by(id=user).first()
        treelist = get_list_for_tree(25, db)

        return render_template('profile/edit.html', first_name=userform.first_name, last_name=userform.last_name, user=userform, page=page, treelist=treelist)


@profile.route('/tickets/<int:id>')
@token_required

def get_ticket(id):
    ticket = db.session.query(Ticket).filter_by(id=id).first()
    return render_template('profile/tickets.html', ticket=ticket, first_name=request.first_name, last_name=request.last_name)