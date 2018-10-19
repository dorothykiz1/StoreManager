from flask import Blueprint, request, json

mod = Blueprint('products', __name__)
products = []


@mod.route('/', methods=['POST'])
def create_product():
    """endpoint to post a product"""
    try:
        data = request.get_json()
        product = dict(
            Id=len(products) + 1,
            title=data['title'],
            description=data['description'],
            quantity=data['quantity']
        )
        products.append(product)
        return json.dumps({'message': 'Product successfully added'}), 201
    except:
        return json.dumps({'message': 'missing arguments ,please try again'})


@mod.route('/', methods=['GET'])
def get_all_products():
    """endpoint to get all products"""
    return json.dumps({"Products": products}), 200


@mod.route('/<int:productId>', methods=['GET'])
def get_single_product(productId):
    """ endpoint to get a single product"""

    for product in products:
        if product['id'] == productId:
            return json.dumps({'Message': product}), 200

    return json.dumps({'Message': 'Sale Id out of range'}), 400
