from flask import Flask,jsonify,request

app = Flask(__name__)

myproducts = []
mysales = []
myusers = []

@app.route("/", methods=["GET"] )
def home():
    return jsonify({"Flask API" : "1.0"}), 200

@app.route("/products", methods=["GET","POST"] )
def products():
    if request.method == "GET":
        return jsonify(myproducts), 200
    
    elif request.method == "POST":
        data = request.get_json()
        myproducts.append(data)
        return jsonify({"message": "Product added successfully"}), 201
    
    else:
        error = {"message": "Method not allowed"}
        return jsonify(error), 405

app.run(debug=True)