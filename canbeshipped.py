from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Calculates and returns the shipping cost for the product."""
        pass