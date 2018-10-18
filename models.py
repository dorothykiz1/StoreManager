class Product:
    """This is a product class"""

    def __init__(self, product_Id, title, description, quantity, price):
        """Initialise with product_Id,title ,description,quantity and price"""
        self.product_Id = product_Id
        self.title = title
        self.description = description
        self.quantity = quantity
        self.price = price

    def create_new_product(self, admin_Id):
        pass

    def get_all_products(self):
        pass

    def get_single_product(self, product_Id):
        pass


class Sale:
    """This is a Sale class"""

    def __init__(self, sale_Id, attendant_Id, attendant_name, admin_Id):
        """Initialise with record_Id ,attendant_Id,admin_Id """
        self.sale_Id = sale_Id
        self.attendant_Id = attendant_Id
        self.admin_Id = admin_Id

    def create_new_sale_record(self):
        pass

    def get_all_sale_records(self, admin_Id):
        pass

    def get_single_sale_record(self, record_Id):
        pass
