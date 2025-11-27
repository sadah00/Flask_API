from flask import Flask,jsonify,request
from models import db,Product,Sales,Purchases

app = Flask(__name__)

# Initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kimysada6@localhost:5432/flask_api'
db.init_app(app)

myproducts = []
mysales = []
myusers = []
mypurchases = []

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

@app.route("/sales", methods=["GET","POST"] )
def sales():
    if request.method == "GET":
        mysales = Sales.query.all() 
        sales_list = []
        for sale in mysales:
            sales_list.append({
                "id": sale.id,
                "product_id": sale.product_id,
                "quantity": sale.quantity,
                "created_at": sale.created_at
            })   
        return jsonify(sales_list), 200
    
    elif request.method == "POST":
        data = request.get_json()
        new_sale=Sales(
            product_id=data['product_id'],
            quantity=data['quantity']
        )
        db.session.add(new_sale)
        db.session.commit()
        data['id'] = new_sale.id
        data['created_at'] = new_sale.created_at
        return jsonify({"message": "Sale recorded successfully"}), 201
    
    else:
        error = {"message": "Method not allowed"}
        return jsonify(error), 405

@app.route("/purchases", methods=["GET","POST"] )
def purchases():
    if request.method == "GET":
        mypurchases = Purchases.query.all() 
        purchases_list = []
        for purchase in mypurchases:
            purchases_list.append({
                "id": purchase.id,
                "product_id": purchase.product_id,
                "stock_quantity": purchase.stock_quantity,
                "created_at": purchase.created_at
            })   
        return jsonify(purchases_list), 200
    
    elif request.method == "POST":
        data = request.get_json()
        new_purchase=Purchases(
            product_id=data['product_id'],
            stock_quantity=data['stock_quantity']
        )
        db.session.add(new_purchase)
        db.session.commit()
        data['id'] = new_purchase.id
        data['created_at'] = new_purchase.created_at
        return jsonify({"message": "Purchase recorded successfully"}), 201
    
    else:
        error = {"message": "Method not allowed"}
        return jsonify(error), 405






if __name__ == "__main__":
    with app.app_context():
        db.create_all()
app.run(debug=True)