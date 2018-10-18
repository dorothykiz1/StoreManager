from flask import Blueprint, request, json
mod = Blueprint('sales', __name__)

products = []


@mod.route('/api/v1/products', methods=['POST'])
def create_product():
    """endpoint to post a product"""

    data = request.get_json()
    product = dict(
        id=len(products)+1,
        title=data['title'],
        description=data['description'],
        quantity=data['quantity'],

    )
    products.append(product)
    return json.dumps({'message': 'Product successfully added'}), 201


# @app.route('/api/v1/products', methods=['GET'])
# def get_all_products():
#     """endpoint to get all products"""
#     return json.dumps({"Products": products}), 200


# @app.route('/api/v1/products/<int:productId>', methods=['GET'])
# def get_single_product(productId):
#     """ endpoint to get a single product"""

#     for product in products:
#         if product['id']== productId:
#             return json.dumps({'Message': product}), 200

#     return json.dumps({'Message': 'product Id out of range'}), 400
