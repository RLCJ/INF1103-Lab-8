from canbeshipped import CanBeShipped
from product import Product
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier,
        weight: float,
    ):
        # Forward product_id, name, price, stock, supplier to the Product parent class
        super().__init__(product_id, name, price, stock, supplier)
        self.weight: float = float(weight)

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight} kg")

    def get_fulfilment_info(self) -> str:
        """Returns a string with fulfilment information specific to physical products."""
        return "Product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        base_fee = 5.0
        rate_per_kg = 2.0
        return base_fee + (self.weight * rate_per_kg)