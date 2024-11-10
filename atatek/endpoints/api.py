from flask import Blueprint, render_template, request, redirect, make_response, url_for
from atatek.db import Tree, db, Config
from atatek.endpoints import auth_bp
from atatek.utils import get_tree_data

api_bp = Blueprint('api', __name__)

@api_bp.route('/start')
def start():
    tree = Tree(
        item_id=14,
        name='Алаш'
    )
    db.session.add(tree)
    db.session.commit()
    return 'nice'

@api_bp.route('/api/get/<id>')
def get_data(id):
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
                items_data.append({
                    'id': tree.id,
                    'name': item['name'],
                    'birth_year': item['birth_year'],
                    'death_year': item['death_year'],
                    'parent_id': node.id,
                    'info': 'have',
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
            items_data.append({
                'id': item.id,
                'name': item.name,
                'birth_year': item.birth_year,
                'death_year': item.death_year,
                'parent_id': node.id,
                'info': 'have',
                'status': 'true'
            })
        response = {
            'status': True,
            'version': 'v2',
            'author': 'baxa',
            'data': items_data
        }
        return response
