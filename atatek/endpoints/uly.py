import json
from flask import Blueprint, request, render_template, url_for, redirect
from atatek.db import Page, db, Tree, TreeInfo
from atatek.endpoints.main import settings_path, token_required
from atatek.utils import get_tree_data
from atatek.utils.get_parent_list import get_list_for_tree

ulyjyz = Blueprint("pages", __name__)

@ulyjyz.route("/uly/<string:bread1>/<string:bread2>/<string:bread3>")
@token_required
def uly(bread1, bread2, bread3):
    page = db.session.query(Page).filter_by(breed1=bread1, breed2=bread2, breed3=bread3).first()
    if page.juz != 'Ұлы жүз':
        return redirect('/')
    res = get_list_for_tree(page.item, db)
    with open(settings_path, 'r') as file:
        settings = json.load(file)

    return render_template('main/index.html', page=page.title, js='page.js', set=settings, start=json.dumps(res))


@ulyjyz.route('/api/get/<id>/childs')
def get_child_data_for_uly(id):
    items_data = []

    node = db.session.query(Tree).filter_by(id=id).first()
    if not node:
        # Если родительский элемент не найден, возвращаем ошибку или обработку случая
        return {'error': 'Parent not found'}, 404

    # Проверяем, есть ли уже дети с данным parent_id
    childs = db.session.query(Tree).filter_by(parent_id=node.id).all()

    if not childs:
        data = get_tree_data(node.item_id)
        for item in data:
            # Проверяем, существует ли уже объект с таким item_id и parent_id
            existing_tree = db.session.query(Tree).filter_by(item_id=item['id'], parent_id=node.item_id).first()
            if not existing_tree:
                tree = Tree(
                    item_id=item['id'],
                    name=item['name'],
                    parent_id=node.id,
                    birth_year=item['birth_year'],
                    death_year=item['death_year'],
                )
                db.session.add(tree)
                db.session.commit()
                info_tree = db.session.query(TreeInfo).filter_by(tree_id=tree.id).first()
                if info_tree:
                    info = 'have'
                else:
                    info = None
                items_data.append({
                    'id': tree.id,
                    'name': item['name'],
                    'birth_year': item['birth_year'],
                    'death_year': item['death_year'],
                    'parent_id': node.id,
                    'info': info,
                    'untouchable': False,
                    'status': 'true'
                })

        response = {
            'status': True,
            'version': 'v2',
            'author': 'baxa',
            'data': items_data
        }
        return response
    else:
        for item in childs:
            info_tree = db.session.query(TreeInfo).filter_by(tree_id=item.id).first()
            if info_tree:
                info = 'have'
            else:
                info = None
            items_data.append({
                'id': item.id,
                'name': item.name,
                'birth_year': item.birth_year,
                'death_year': item.death_year,
                'parent_id': node.id,
                'info': info,
                'untouchable': False,
                'status': 'true'
            })
        response = {
            'status': True,
            'version': 'v2',
            'author': 'baxa',
            'data': items_data
        }
        return response