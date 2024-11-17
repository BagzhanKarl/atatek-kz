from atatek.db import db, Role
from flask import Blueprint, render_template, request, url_for, redirect

from atatek.endpoints.main import token_required

admin = Blueprint('Admin', __name__)

@admin.route('/')
@token_required
def admin_index():
    role = request.role

    if role != 5:
        return redirect(url_for('Main.mainpage'))
    else:
        return render_template('admin/index.html')

@admin.route('/settings')
@token_required
def admin_settings():
    return render_template('admin/settings.html')

@admin.route('/packs')
@token_required
def admin_packs():
    roles = db.session.query(Role).all()
    return render_template('admin/packs.html', roles=roles)