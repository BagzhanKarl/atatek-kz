from flask import Blueprint, render_template, request

from atatek.endpoints.main import token_required

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@token_required
def profile_file():
    page = request.page
    return render_template('profile/profile.html', page=page)