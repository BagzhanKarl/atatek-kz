from flask import Blueprint, render_template, request, redirect, make_response, url_for, jsonify
from sqlalchemy.sql.functions import user

from atatek.db import Tree, db, Config, TreeInfo, Ticket
from atatek.endpoints import auth_bp
from atatek.endpoints.main import token_required
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

@api_bp.route('/api/get/<id>/childs')
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
                'status': 'true'
            })
        response = {
            'status': True,
            'version': 'v2',
            'author': 'baxa',
            'data': items_data
        }
        return response

@api_bp.route('/api/get/<int:id>/info', methods=['POST'])
@token_required
def get_info_tree(id):
    role = request.role
    item = db.session.query(Tree).filter_by(id=id).first()
    item_more = db.session.query(TreeInfo).filter_by(tree_id=id).first()

    return render_template('modals/info.html', role=role, item=item, item_more=item_more)

@api_bp.route('/api/add/childs/<int:id>', methods=['POST'])
@token_required
def add_child(id):
    user = request.user_id
    role = request.role
    childs = request.form.getlist('childname[]')
    for child in childs:
        ticket = Ticket(
            created_by=user,
            name_new=child,
            parent=id,
            type='add',
        )
        db.session.add(ticket)
    db.session.commit()
    return redirect('/my/tickets')

@api_bp.route('/api/edit/<int:id>', methods=['POST'])
@token_required
def edit_ticket(id):
    user = request.user_id
    name = request.form.get('name')  # Обязательное поле

    # Необязательные поля
    birth_year = request.form.get('birth', None)
    death_year = request.form.get('death', None)
    info = request.form.get('info', None)

    # Создаем объект Ticket с использованием значений, если они заданы
    ticket = Ticket(
        created_by=user,
        type='edit',
        name=name,
        birth=birth_year,
        death=death_year,
        info=info,
        tree_id=id
    )
    db.session.add(ticket)
    db.session.commit()
    return redirect('/my/tickets')