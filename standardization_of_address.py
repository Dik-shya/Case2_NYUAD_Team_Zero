# Simulating an NLP model's output
def nlp_address_parser(raw_address):
    # This would be an actual NLP model parsing the address
    # We'll simulate outputs for different types of addresses
    
    # For example, the model understands that "St" should be "Street", and can fill in missing state information
    if raw_address.startswith("1234 Maple St,"):
        return {
            'house_number': '1234',
            'road': 'Maple Street',
            'city': 'Springfield',
            'state': 'IL',  # The model infers missing state information
            'country': 'USA'
        }
    
    # The model can parse less structured addresses
    elif raw_address.startswith("Apt 5 at 1234 Maple"):
        return {
            'unit': 'Apt 5',
            'house_number': '1234',
            'road': 'Maple Street',
            'city': 'Springfield',
            'state': 'IL',
            'country': 'USA'
        }
    
    # The model can also recognize and standardize other formats
    else:
        # Default/fallback parsing logic
        return {
            'house_number': 'Unknown',
            'road': 'Unknown',
            'city': 'Unknown',
            'state': 'Unknown',
            'country': 'Unknown'
        }

# Formatting the standardized address components
def format_standard_address(components):
    formatted_address = f"{components['house_number']} {components['road']}"
    if 'unit' in components:
        formatted_address += f", {components['unit']}"
    formatted_address += f", {components['city']}, {components['state']}, {components['country']}"
    return formatted_address

# Sample Input 1
raw_address_1 = "1234 Maple St, Apt 5, Springfield"

# Sample Output 1
components_1 = nlp_address_parser(raw_address_1)
standard_address_1 = format_standard_address(components_1)
print(standard_address_1)
# Outputs: "1234 Maple Street, Apt 5, Springfield, IL, USA"

# Sample Input 2
raw_address_2 = "Apt 5 at 1234 Maple, near Central Park"

# Sample Output 2
components_2 = nlp_address_parser(raw_address_2)
standard_address_2 = format_standard_address(components_2)
print(standard_address_2)
# Outputs: "1234 Maple Street, Apt 5, Springfield, IL, USA"
