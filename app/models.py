from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user



class User(UserMixin,db.Model):
    __tablename__='users'

    id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    products = db.relationship('Product', backref='user', lazy='dynamic')
  
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'



class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name= db.Column(db.String(255),nullable = False)
    description = db.Column(db.Text(), nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    size = db.Column(db.String(), nullable = False)
    image=db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))





    
    def save_p(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Product {self.post}'
