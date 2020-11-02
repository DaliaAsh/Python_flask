from flask import Flask , render_template , url_for , request ,redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Product(db.Model):
    product_id = db.Column(db.String(50),primary_key= True)
    


class Location(db.Model):
    location_id = db.Column(db.String(50),primary_key= True)    
    

class ProductMovement(db.Model):
    movement_id = db.Column(db.String(50),primary_key= True) 
    timestamp = db.Column(db.DateTime,default=datetime.now)
    from_location = db.Column(db.String(50), db.ForeignKey('location.location_id'),default="") 
    to_location = db.Column(db.String(50), db.ForeignKey('location.location_id'),default="")
    product_id = db.Column(db.String(50), db.ForeignKey('product.product_id'),default="") 
    qty = db.Column(db.Integer)  

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/product',methods=['POST','GET'])
def product():
    if request.method == 'POST':
         product_id = request.form['product_id']
         new_product=Product(product_id=product_id)
         db.session.add(new_product)
         db.session.commit()
         return redirect('/product')
        
       
    if request.method == 'GET':    
        products= Product.query.order_by(Product.product_id).all()
        return render_template('product.html',products=products)

@app.route('/delete-product/<id>')
def delete_product(id):
    to_delete_product = Product.query.get_or_404(id)
    try:
        db.session.delete(to_delete_product)
        db.session.commit()
        return redirect('/product')
    except:
        return 'A probelm deleting product'    

@app.route('/update-product/<id>/<updated_id>')
def edit_product(id,updated_id):
    product = Product.query.filter_by(product_id=id).first()
    product.product_id = updated_id 
    db.session.commit()
    return redirect('/product')


@app.route('/location',methods=['POST','GET'])
def location():
    if request.method == 'POST':
         location_id = request.form['location_id']
         new_location=Location(location_id=location_id)
         db.session.add(new_location)
         db.session.commit()
         return redirect('/location')
        
       
    if request.method == 'GET':    
        locations= Location.query.order_by(Location.location_id).all()
        return render_template('location.html',locations=locations)

@app.route('/delete-location/<id>')
def delete_location(id):
    to_delete_location = Location.query.get_or_404(id)
    try:
        db.session.delete(to_delete_location)
        db.session.commit()
        return redirect('/location')
    except:
        return 'A probelm deleting location'    

@app.route('/update-location/<id>/<updated_id>')
def edit_location(id,updated_id):
    location = Location.query.filter_by(location_id=id).first()
    location.location_id = updated_id 
    db.session.commit()
    return redirect('/location')


@app.route('/movement',methods=['POST','GET'])
def movement():
    if request.method == 'POST':
         movement_id = request.form['movement_id']
         location_group = request.form['location-group']
         location = request.form['location']
         product_id = request.form['product_id']
         qty = request.form['qty']
         if location_group == 'from':
            new_movement=ProductMovement(movement_id=movement_id,from_location=location,to_location="",product_id=product_id,qty=qty)
         else:
             new_movement=ProductMovement(movement_id=movement_id,from_location="",to_location=location,product_id=product_id,qty=qty)
         db.session.add(new_movement)
         db.session.commit()
         return redirect('/movement')
        
       
    if request.method == 'GET':    
        movements= ProductMovement.query.order_by(ProductMovement.movement_id).all()
        return render_template('movement.html',movements=movements)

@app.route('/delete-movement/<id>')
def delete_movement(id):
    to_delete_movement = ProductMovement.query.get_or_404(id)
    try:
        db.session.delete(to_delete_movement)
        db.session.commit()
        return redirect('/movement')
    except:
        return 'A probelm deleting movement'    

@app.route('/update-movement/<id>/<updated_id>')
def edit_movement(id,updated_id):
    movement = ProductMovement.query.filter_by(movement_id=id).first()
    movement.movement_id = updated_id 
    db.session.commit()
    return redirect('/movement')
