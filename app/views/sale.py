from flask import Flask, json, request

app = Flask(__name__)
sales = []


# @app.route('/api/v1/sales', methods=['POST'])
# def create_new_sale():
#     """endpoint to post a sale_record"""

#     data = request.get_json()
#     sale = dict(
#         saleId=len(sales)+1,
#         attendant_Id=data['attendant_Id']
#     )
#     sales.append(sale)
#     return json.dumps({'message': 'sale record successfully made'}), 201


@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    """endpoint to get all sale records"""
    return json.dumps({"sales": sales}), 200


# @app.route('/api/v1/sales/<int:saleId>', methods=['GET'])
# def get_single_sale_record(saleId):
#     """ endpoint to get a single sale"""

#     for sale in sales:
#         if sale.saleId == saleId:
#             sale_dict = {
#                 'sale_record_Id': sale.sale_record_Id,
#                 'attendant_Id': sale.attendant_Id
#             }
#             sales.append(sale_dict)
#     # return json.dumps({'Message': "Your request is successful"}), 200
#         if sale not in sales:
#             return {'message': 'sale not made'}, 200
#         else:
#             return json.dumps({'sale made': sale_dict})

#             # return json.dumps({'sale': sales[saleId]}), 200
