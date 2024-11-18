from atatek.db import Tree, TreeInfo

def get_list_for_tree(id, db):
    item = id
    result = []

    while True:
        start = db.session.query(Tree).filter_by(id=item).first()
        if not start:
            break  # Если элемент не найден, выходим из цикла
        if start.id == id:
            info = None
            treeinfo = db.session.query(TreeInfo).filter_by(tree_id=start.id).first()
            if treeinfo:
                info = 'Have'
            result.append({
                "id": start.id,
                "name": start.name,
                "untouchable": False,
                "gender": 'M',
                "status": 'notmy',
                "born": None,
                "death": None,
                "info": info,
                "parent": start.parent_id if start.parent_id is not None else "",  # Заменить на пустую строку, если родитель не найден
            })
        else:
            result.append({
                "id": start.id,
                "name": start.name,
                "untouchable": True,
                "gender": 'M',
                "status": 'notmy',
                "born": None,
                "death": None,
                "info": None,
                "parent": start.parent_id if start.parent_id is not None else "",  # Заменить на пустую строку
            })
        parent = db.session.query(Tree).filter_by(id=start.parent_id).first()
        if parent:
            item = parent.id  # Переходим к родителю
        else:
            break  # Если родителя нет, выходим из цикла

    return result[::-1]
