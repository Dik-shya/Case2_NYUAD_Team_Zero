import re

def standardize_address(raw_address):
    # Assume we have a trained NLP model that can extract components of an address.
    # Here, we are simulating it with regex for demonstration purposes.
    address_components = re.match(r'(\d+)\s+(.*?),\s*(Apt|Suite)\s*(\d+),\s*(.*)', raw_address)
    standardized_address = {
        'number': address_components.group(1),
        'street': address_components.group(2),
        'unit_type': address_components.group(3),
        'unit_number': address_components.group(4),
        'city': address_components.group(5)
    }
    return standardized_address

# Sample Input
raw_address = "1234 Maple Street, Apt 5, Springfield"

# Sample Output
standard_address = standardize_address(raw_address)
print(standard_address)
# Outputs: {'number': '1234', 'street': 'Maple Street', 'unit_type': 'Apt', 'unit_number': '5', 'city': 'Springfield'}
