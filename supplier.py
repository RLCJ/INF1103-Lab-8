class Supplier:
    """Represents a supplier providing products to the inventory system."""

    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.supplier_id = str(supplier_id)
        self.name = str(name)
        self.contact_email = str(contact_email)

    def display_information(self) -> None:
        """Displays formatted details about the supplier."""
        print(f"Supplier ID: {self.supplier_id} | Name: {self.name} | Contact: {self.contact_email}")