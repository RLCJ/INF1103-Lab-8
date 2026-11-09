from product import Product

class Inventory:
    def __init__(self):
        # Stores a collection of Product objects
        self.products = []

    def add_product(self, product):
        """Adds a Product object to the inventory collection."""
        self.products.append(product)

    def display_all(self):
        """Displays all products managed by the inventory."""
        if not self.products:
            print("Inventory is currently empty.\n")
            return
            
        print("Current Inventory")
        print("-" * 40)
        for prod in self.products:
            # Calls the display method belonging to each individual Product object
            prod.display_information()
        print("-" * 40)

    def search_product(self, query):
        """Searches for products in the collection by ID or name."""
        query = query.strip().lower()
        found = False
        
        for prod in self.products:
            if query in prod._product_id.lower() or query in prod.name.lower():
                prod.display_information()
                found = True
                
        if not found:
            print("No matching product found.\n")