from flask import Blueprint
from sqlalchemy import text
from atatek.db import db

tests = Blueprint('TEST', __name__)

@tests.route('/test/baxa/count')
def baxa_count():
    query = """
        WITH RECURSIVE descendants AS (
            SELECT id
            FROM tree
            WHERE id = 2  -- Это id Улы жуз
            UNION ALL
            SELECT t.id
            FROM tree t
            INNER JOIN descendants d ON t.parent_id = d.id
        )
        SELECT COUNT(*) 
        FROM descendants;
        """
    result = db.session.execute(text(query))
    count = result.scalar()
    print(count)
    return f"Количество потомков для Улы жуз: {count}"