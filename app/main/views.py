from . import main
from flask import render_template,request,redirect,url_for,abort
from .. import db,photos
from flask_login import login_required,current_user
from ..models import Product, User
from werkzeug.utils import secure_filename


from .forms import ProductForm

@main.route('/')
def index():


    return render_template('main/index.html')

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