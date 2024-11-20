import uuid
from atatek.db import db, Role, Page, User, News
from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from atatek.db.models.pages import Moderator
from atatek.endpoints.main import token_required
import os
from werkzeug.utils import secure_filename

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

@admin.route('/sites')
@token_required
def admin_sites():
    pages = db.session.query(Page).all()
    return render_template('admin/sites.html', pages=pages)

@admin.route('/site/<int:id>')
@token_required
def admin_site(id):
    page = db.session.query(Page).filter_by(id=id).first()
    moderators = db.session.query(Moderator).filter_by(page=page.id).all()
    moderatorList = []
    if moderators:
        for moderator in moderators:
            user = db.session.query(User).filter_by(id=moderator.user).first()
            moderatorList.append({
                "id": user.id,
                "first_name": user.fist_name,
                "last_name": user.last_name,
            })

    return render_template('admin/site.html', page=page, moderator=moderatorList)

@admin.route('/site/<int:id>/save_news', methods=['POST'])
@token_required
def save_news_admin(id):
    title = request.form.get('title')
    page = request.form.get('page')
    content = request.form.get('content')
    image = request.files.get('poster')

    # Безопасное сохранение файла
    if image:
        filename = secure_filename(image.filename)
        # Добавление уникального префикса, например, timestamp
        ext = os.path.splitext(filename)[1]
        unique_filename = f"{uuid.uuid4()}{ext}"
        save_path = os.path.join('atatek', 'static', 'images', 'news', unique_filename)
        image.save(save_path)


    news = News(
        page=id,
        title=title,
        content=content,
        poster=unique_filename
    )
    db.session.add(news)
    db.session.commit()
    return jsonify({"status": True})
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
    return redirect(url_for('Admin.admin_sites'))

@admin.route('/tickets')
def ticket_list():
    return render_template('admin/tickets.html')