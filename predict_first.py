from supplier import Supplier
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

# 1. Create Supplier first
sup = Supplier("SUP01", "Test", "orders@techdistro.com")

# 2. Pass arguments in exact order: (id, name, price, stock, supplier, weight)
p = PhysicalProduct("P8001", "Cat", 1500.00, 10, sup, 9.5)

p.display_information()