
from flask import Blueprint, request, json
mod = Blueprint('sales', __name__)
sales = []


@mod.route('/', methods=['POST'])
def create_new_sale():
    """endpoint to post a new sale_record"""

    data = request.get_json()
    sale = dict(
        id=len(sales)+1,
        attendant_Id=data['attendant_Id'],
        attendant_name=data['attendant_name'],
    )
    sales.append(sale)
    return json.dumps({'message': sale}), 201


@mod.route('/', methods=['GET'])
def get_all_sales():
    """endpoint to get all sale records"""
    return json.dumps({"sales": sales}), 200


@mod.route('/<int:saleId>', methods=['GET'])
def get_single_sale_record(saleId):
    """ endpoint to get a single sale"""
    for sale in sales:
        if sale['id'] == saleId:
            return json.dumps({'Message': sale}), 200

    return json.dumps({'Message': 'Sale Id out of range'}), 400
