from flask import Blueprint, jsonify
from atatek.db import Tree, Role, db, Page

startInstall = Blueprint('start', __name__)

@startInstall.route('/start/install')
def start():
    tree = Tree(
        item_id=14,
        name='Алаш'
    )
    db.session.add(tree)
    roles = [
        {
            "title": "Бастау",
            "js": "bastay.js",
            "addchild": 0,
            "addinfo": 0,
        },
        {
            "title": "Сарапшы",
            "js": "sarapshy.js",
            "addchild": 0,
            "addinfo": 0,
        },
        {
            "title": "Алтын",
            "js": "altyn.js",
            "addchild": 0,
            "addinfo": 0,
        },
        {
            "title": "Модератор",
            "js": "moderator.js",
            "addchild": 0,
            "addinfo": 0,
        },
        {
            "title": "Администратор",
            "js": "admin.js",
            "addchild": 0,
            "addinfo": 0,
        },
    ]
    for role in roles:
        roleItem = Role(
            title=role['title'],
            js=role['js'],
            add_child=role['addchild'],
            add_info=role['addinfo'],
        )
        db.session.add(roleItem)
    page = Page(
        title='Start',
        breed1='start',
        breed2='start',
        breed3='start',
        juz='start',
        item=1,
    )
    db.session.add(page)
    db.session.commit()
    return jsonify({"status": True, "data": "Установка завершено"})