from itertools import product
from flask import Flask, json, jsonify, request

app = Flask(__name__)

#Importar lista de productos
from products import products

#Crear Rutas
@app.route('/ping')
def ping():
    return jsonify({"mensage":"pong"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Lista de Productos"})

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productFound = [product for product in products if product['name']== product_name]
    if (len(productFound) > 0 ):
        return jsonify({"product": productFound[0]})
    return jsonify({"message:":"producto no encontrado"})

@app.route('/products', methods=['POST'])
def addProducts():
    new_product ={
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity":  request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message":"Producto Agregado Correctamente: ", "Producto": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name']== product_name]
    if (len(productFound)>0):
        productFound[0]['name']= request.json['name']
        productFound[0]['price']= request.json['price']
        productFound[0]['quantity']= request.json['quantity']
        return jsonify(
            {"message": "Producto Actualizado",
            "product": productFound[0]})
    return jsonify({"message": "Producto no encontrado"})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProducts(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound)>0):
        products.remove(productFound[0])
        return jsonify({"message":"Producto Eliminado", "productos": products}) 
    return jsonify({"message":"Producto No Encontrado"})


#inicializar:
if __name__ == '__main__':
    app.run(debug=True, port=3000)