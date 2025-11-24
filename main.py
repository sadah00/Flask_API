from flask import Flask,jsonify,request
from models import db,Product

app = Flask(__name__)

# Initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kimysada6@localhost:5432/flask_api'
db.init_app(app)

myproducts = []
mysales = []
myusers = []

@app.route("/", methods=["GET"] )
def home():
    return jsonify({"Flask API" : "1.0"}), 200

@app.route("/products", methods=["GET","POST"] )
def products():
    if request.method == "GET":
        myproducts = Product.query.all() 
        products_list = []
        for product in myproducts:
            products_list.append({
                "id": product.id,
                "name": product.name,
                "buying_price": product.buying_price,
                "selling_price": product.selling_price
            })   
        return jsonify(products_list), 200
    
    elif request.method == "POST":
        data = request.get_json()
        new_product=Product(
            name=data['name'],
            buying_price=data['buying_price'],
            selling_price=data['selling_price']
        )
        db.session.add(new_product)
        db.session.commit()
        data['id'] = new_product.id
        return jsonify({"message": "Product added successfully"}), 201
    
    else:
        error = {"message": "Method not allowed"}
        return jsonify(error), 405


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
app.run(debug=True)