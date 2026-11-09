import json
import os
from inventory import Inventory
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

FILE_NAME = "inventory.json"


def load_inventory(inventory_obj):
    """Loads inventory from JSON file if present; otherwise loads default products."""
    if os.path.exists(FILE_NAME):
        print(f"{FILE_NAME} found.")
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                for item in data:
                    # Reconstruct specific subclass instances based on product_type
                    prod_type = item.get("product_type", "physical")
                    if prod_type == "digital":
                        prod = DigitalProduct(
                            item["id"], item["name"], item["price"],
                            item["stock"], item.get("file_size", 0.0)
                        )
                    else:
                        prod = PhysicalProduct(
                            item["id"], item["name"], item["price"],
                            item["stock"], item.get("weight", 0.0)
                        )
                    inventory_obj.add_product(prod)
            print("Inventory loaded successfully.\n")
        except Exception as e:
            print(f"Error loading {FILE_NAME}: {e}. Loading default data.\n")
            load_default_data(inventory_obj)
    else:
        print(f"{FILE_NAME} not found. Creating new inventory...\n")
        load_default_data(inventory_obj)
        save_inventory(inventory_obj)


def load_default_data(inventory_obj):
    """Loads default product objects (both Physical and Digital) into inventory."""
    default_products = [
        PhysicalProduct("8001", "Gaming Laptop", "$1500.00", 10, 2.5),
        PhysicalProduct("8002", "Mechanical Keyboard", "$80.00", 25, 0.9),
        DigitalProduct("8003", "Photo Editor Pro", "$49.99", 100, 750.5),
        DigitalProduct("8004", "Antivirus Security Suite", "$29.99", 200, 150.0),
    ]
    for prod in default_products:
        inventory_obj.add_product(prod)


def save_inventory(inventory_obj):
    """Saves the current inventory collection to inventory.json including subclass attributes."""
    data = []
    for prod in inventory_obj.products:
        item_data = {
            "id": prod._product_id,
            "name": prod.name,
            "price": prod._price,
            "stock": prod.stock,
        }
        
        # Save specific attributes depending on object type
        if isinstance(prod, PhysicalProduct):
            item_data["product_type"] = "physical"
            item_data["weight"] = prod.weight
        elif isinstance(prod, DigitalProduct):
            item_data["product_type"] = "digital"
            item_data["file_size"] = prod.file_size

        data.append(item_data)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_product_workflow(inventory_obj):
    """Handles user input to create either a PhysicalProduct or DigitalProduct."""
    max_id = 8000
    for prod in inventory_obj.products:
        try:
            prod_num = int(prod._product_id)
            if prod_num > max_id:
                max_id = prod_num
        except ValueError:
            pass
    new_id = str(max_id + 1)

    # 1. Choose Product Type
    print("Select Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")
    while True:
        type_choice = input("Enter type (1 or 2): ").strip()
        if type_choice in ["1", "2"]:
            break
        print("Invalid choice. Please enter 1 or 2.")

    # 2. Get Product Name
    while True:
        name = input("Enter product name: ").strip()
        if not name:
            print("Error: Product name cannot be empty. Please try again.")
        elif name.isdigit():
            print("Error: Product name cannot be just numbers. Please enter a valid name.")
        else:
            break

    # 3. Get Price
    while True:
        price_input = input("Enter product price ($): ").strip()
        try:
            price_val = float(price_input)
            if price_val <= 0:
                print("Error: Price must be greater than $0.00. Please try again.")
            else:
                price = f"${price_val:.2f}"
                break
        except ValueError:
            print("Error: Invalid price. Please enter a valid decimal number.")

    # 4. Get Stock
    while True:
        stock_input = input("Enter initial stock: ").strip()
        if stock_input.isdigit():
            stock = int(stock_input)
            break
        print("Error: Invalid stock amount. Please enter a valid integer.")

    # 5. Get Subclass Specific Attribute and Create Object
    if type_choice == "1":
        while True:
            try:
                weight = float(input("Enter weight (kg): ").strip())
                if weight <= 0:
                    print("Weight must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical weight.")
        
        new_product = PhysicalProduct(new_id, name, price, stock, weight)

    else:
        while True:
            try:
                size = float(input("Enter download size (MB): ").strip())
                if size <= 0:
                    print("Download size must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical file size.")

        new_product = DigitalProduct(new_id, name, price, stock, size)

    # Delegate object addition to Inventory class
    inventory_obj.add_product(new_product)
    print(f"Product '{name}' added successfully with ID: {new_id}.\n")


def update_stock_workflow(inventory_obj):
    """Finds a product by ID and updates its stock through the product's own method."""
    prod_id = input("Enter product ID to update: ").strip()
    for prod in inventory_obj.products:
        if prod._product_id == prod_id:
            try:
                added_stock = int(input(f"Enter stock to add for {prod.name}: "))
                if added_stock < 0:
                    print("Stock cannot be negative.\n")
                    return
                # Delegate stock update logic to the product instance (Encapsulation)
                prod.update_stock(added_stock)
                print()
                return
            except ValueError:
                print("Invalid stock number.\n")
                return
    print("Product ID not found.\n")


def print_menu():
    print("---------------- MENU ----------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------------------")


def main():
    print("=========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=========================================\n")

    my_inventory = Inventory()
    load_inventory(my_inventory)

    while True:
        print_menu()
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            print()
            my_inventory.display_all()
            print()
        elif choice == "2":
            print()
            add_product_workflow(my_inventory)
            print()
        elif choice == "3":
            print()
            update_stock_workflow(my_inventory)
            print()
        elif choice == "4":
            print()
            query = input("Enter Product ID or Name to search: ")
            my_inventory.search_product(query)
            print()
        elif choice == "5":
            save_inventory(my_inventory)
            print("Inventory saved to inventory.json.\n")
        elif choice == "6":
            save_inventory(my_inventory)
            print("Saving inventory before exit...\nInventory saved successfully!")
            print("Thank you for using the Inventory Management System")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()