from flask import render_template,request,redirect,url_for,abort,flash
from . import main
# from ..requests import 
from ..models import User
from .forms import UpdateProfile
from ..models import Product, User
# from .. import db,photos

from flask_login import login_required,current_user

@main.route('/')
def index():


    return render_template('main/index.html')

@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        return ('not found')
    return render_template('profile/profile.html', user=user)

@main.route('/user/<name>/update_profile', methods=['POST', 'GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        error = 'The user does not exist'
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('profile/update_profile.html', form=form)