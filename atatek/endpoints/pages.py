import json
from flask import Blueprint, request, render_template, url_for, redirect
from atatek.db import Page, db
from atatek.endpoints.main import settings_path
from atatek.utils.get_parent_list import get_list_for_tree

ulyjyz = Blueprint("pages", __name__)

@ulyjyz.route("/uly/<string:bread1>/<string:bread2>/<string:bread3>")
def uly(bread1, bread2, bread3):
    page = db.session.query(Page).filter_by(breed1=bread1, breed2=bread2, breed3=bread3).first()
    if page.jyz != 'Ұлы жүз':
        return redirect('/')
    res = get_list_for_tree(page.item, db)
    with open(settings_path, 'r') as file:
        settings = json.load(file)

    return render_template('main/index.html', page=page.title, js='bastay.js', set=settings, start=json.dumps(res))
