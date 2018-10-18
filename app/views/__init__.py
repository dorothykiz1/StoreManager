from flask import Flask
from app.views import product
# from app.views import sale

app = Flask(__name__)
app.register_blueprint(product.mod, url_prefix='/api/v1/products')
# app.register_blueprint(sale.mod, url_prefix='/api/v1/sales')
