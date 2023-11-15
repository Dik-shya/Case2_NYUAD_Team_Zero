def measure_kpis(deliveries_data):
    # Assuming deliveries_data is a list of dictionaries with delivery accuracy and on-time status
    total_deliveries = len(deliveries_data)
    accurate_deliveries = sum(1 for delivery in deliveries_data if delivery['is_accurate'])
    on_time_deliveries = sum(1 for delivery in deliveries_data if delivery['is_on_time'])
    
    accuracy_rate = accurate_deliveries / total_deliveries
    on_time_rate = on_time_deliveries / total_deliveries
    
    kpis = {
        'accuracy_rate': accuracy_rate,
        'on_time_rate': on_time_rate
    }
    return kpis

# Sample Input
deliveries_data = [
    {'is_accurate': True, 'is_on_time': True},
    {'is_accurate': False, 'is_on_time': True},
    {'is_accurate': True, 'is_on_time': False},
    # ... more delivery data ...
]

# Sample Output
kpis = measure_kpis(deliveries_data)
print(kpis)
# Outputs: {'accuracy_rate': 0.66, 'on_time_rate': 0.66}
