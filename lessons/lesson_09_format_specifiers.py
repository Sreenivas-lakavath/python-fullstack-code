# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# format specifiers = {value:flags} format value based on what flags are inserted
item1 = 3000.56
item2 = 96542.2345
item3 = -8564.526

print(f"the item values is ${item1:+,.2f}")
print(f"the item values is ${item2:+,.2f}")
print(f"the item values is ${item1:+,.2f}")
print(f"the item values is ${item2:100}")
print(f"the item values is ${item3:>}")