from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id, name, price, stock, supplier):

        # Encapsulation: Using a leading underscore for private convention 
        self._product_id = product_id
        self.name = name

        if isinstance(price, str):
            price = price.replace("$", "")
        self._price = float(price)
        self.stock = int(stock)
        self.supplier = supplier

    def update_stock(self, quantity):
        """Updates the stock securely through a controlled method."""
        if self.stock + quantity < 0:
            print("Error: Stock cannot fall below zero.")
        else:
            self.stock += quantity
            print(f"Stock updated successfully! New stock for {self.name}: {self.stock}")

    def display_information(self):
        """Displays the product's details neatly."""
        print(f"ID: {self._product_id} | Name: {self.name} | Price: ${self._price:.2f} | Stock: {self.stock}")
        self.supplier.display_information()


    @abstractmethod
    def get_fulfilment_info(self):
        pass