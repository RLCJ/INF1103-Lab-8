from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, file_size, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.file_size = float(file_size)  # File size in MB

    def display_information(self):
        super().display_information()  # Call the base class method to display common product info
        print(f"File Size: {self.file_size} MB")

    def get_fulfilment_info(self):
        return f"Product requires digital delivery. File size: {self.file_size} MB."