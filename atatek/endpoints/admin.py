from atatek.db import db, Role, Page
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


@admin.route('/newsite/', methods=['POST'])
def open_site():
    title = request.form['title']
    item_id = request.form['item']
    jyz = request.form['jyz']
    breed1 = request.form['breed1']
    breed2 = request.form['breed2']
    breed3 = request.form['breed3']

    page = Page(
        title=title,
        item=item_id,
        juz=jyz,
        breed1=breed1,
        breed2=breed2,
        breed3=breed3
    )
    db.session.add(page)
    db.session.commit()
    return redirect(url_for('Admin.admin_index'))
