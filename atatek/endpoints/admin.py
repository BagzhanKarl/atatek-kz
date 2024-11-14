from atatek.db import db
from flask import Blueprint, render_template, request, url_for

admin = Blueprint('admin', __name__)

@admin.route('/')
def admin_index():
    return render_template('admin/index.html')

@admin.route('/settings')
def admin_settings():
    return render_template('admin/settings.html')