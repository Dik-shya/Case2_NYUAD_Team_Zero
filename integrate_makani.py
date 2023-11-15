def integrate_makani(standard_address):
    # Assume we have a database function that can find a Makani number for the given address.
    # Here, we are simulating a database lookup.
    makani_database = {
        ('1234', 'MAPLE STREET', 'SPRINGFIELD'): '1234567890'
    }
    makani_number = makani_database.get(
        (standard_address['number'], standard_address['street'].upper(), standard_address['city'].upper()),
        None
    )
    return makani_number

# Sample Input & Output
makani_number = integrate_makani(standard_address)
print(makani_number)
# Outputs: '1234567890'
