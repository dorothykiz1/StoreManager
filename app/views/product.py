from flask import Flask, json, request

app = Flask(__name__)
products = []


# @app.route('/api/v1/products', methods=['POST'])
# def create_product():
#     """endpoint to post a product"""

#     data = request.get_json()
#     product = dict(
#         Id=len(products) + 1,
#         category=data['category'],
#         description=data['description'],
#         quantity=data['quantity']
#     )
#     products.append(product)
#     return json.dumps({'message': 'Product successfully added'}), 201


@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    """endpoint to get all products"""
    return json.dumps({"Products": products}), 200


# @app.route('/api/v1/products/<int:productId>', methods=['GET'])
# def get_single_product(productId):
#     """ endpoint to get a single product"""

#     for product in products:
#         if product.productId == productId:
#             product_dict = {
#                 'category': product.category,
#                 'description': product.description,
#                 'quantity': product.quantity
#             }
#             products.append(product_dict)
#     # return json.dumps({'Message': "Your request is successful"}), 200
#         if product not in products:
#             return {'message': 'product not in inventory'}, 200
#         else:
#             return json.dumps({'product': products[productId]}), 200
