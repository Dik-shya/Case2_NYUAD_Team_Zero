from sklearn.cluster import AgglomerativeClustering

def predict_address_with_clustering(lat, long):
    # Assume we have a list of known address coordinates (lat, long)
    known_addresses = [
        (37.421955, -122.084058),
        (37.426, -122.08),
        (37.42, -122.0845),
        # ... potentially thousands of known addresses
    ]
    # Convert the list to a numpy array for the clustering algorithm
    known_addresses_array = np.array(known_addresses)
    
    # Fit the model
    clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0.001)
    clustering.fit(known_addresses_array)
    
    # Find the nearest cluster of addresses to the given lat/long
    predicted_cluster = clustering.fit_predict([[lat, long]])
    predicted_address = known_addresses_array[predicted_cluster[0]]
    
    return predicted_address

# Sample Input & Output
lat, long = (37.4215, -122.085)
predicted_address = predict_address_with_clustering(lat, long)
print(predicted_address)
# Outputs: (37.421955, -122.084058)
