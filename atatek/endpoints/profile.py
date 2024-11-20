from flask import Blueprint, render_template, request

from atatek.db import db
from atatek.db import Ticket
from atatek.endpoints.main import token_required
from atatek.utils.get_parent_list import get_list_for_tree

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@token_required
def profile_file():
    user = request.user_id
    page = request.page
    tickets = db.session.query(Ticket).filter_by(created_by=user).order_by(Ticket.created_at.desc()).all()
    treelist = get_list_for_tree(25, db)
    return render_template('profile/profile.html', first_name=request.first_name, last_name=request.last_name, tickets=tickets, page=page, id=user, treelist=treelist)

@profile.route('/tickets/<int:id>')
@token_required

def get_ticket(id):
    ticket = db.session.query(Ticket).filter_by(id=id).first()
    return render_template('profile/tickets.html', ticket=ticket, first_name=request.first_name, last_name=request.last_name)