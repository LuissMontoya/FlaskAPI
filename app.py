from flask import Flask, json, jsonify

app = Flask(__name__)

#Importar lista de productos
from products import products


#Crear Rutas
@app.route('/ping')
def ping():
    return jsonify({"mensage":"pong"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name']== product_name]
    if (len(productFound) > 0 ):
        return jsonify({"product": productFound[0]})
    return jsonify({"message:":"producto no encontrado"})


#inicializar:
if __name__ == '__main__':
    app.run(debug=True, port=3000)