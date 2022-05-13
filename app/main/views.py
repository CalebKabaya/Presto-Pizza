from . import main

# from ..requests import 
from .forms import UpdateProfile
from ..models import Product, User
# from .. import db,photos

from flask_login import login_required,current_user

from flask import render_template,request,redirect,url_for,abort
from .. import db
from flask_login import login_required,current_user

from werkzeug.utils import secure_filename


from .forms import ProductForm


@main.route('/')
def index():


    return render_template('main/index.html')


@main.route('/products')
@login_required
def product():
  
    
    user = current_user._get_current_object().id
    return render_template('pizza_display.html', product=product,  user=user)


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

@main.route('/create_new', methods = ['POST','GET'])
def new_pitch():
    form = ProductForm()
    if form.validate_on_submit():
        name = form.name.data
        description= form.description.data
        size  = form.size .data
        submit  = form.submit .data
        new_product_object = Product(description=description,user_id=current_user._get_current_object().id, size= size,name =name, submit= submit )
        new_product_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('main/addproduct.html', form = form)  

# @main.route('/create_new', methods = ['POST'])
# def update_pic(uname):
#     images = Product.query.filter_by(name = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         images.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

