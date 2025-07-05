import pandas as pd

# Property dataset
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb', 'Rural'],
    'bedrooms': [3, 5, 4, 6, 2],
    'area_sqft': [1500, 2500, 1800, 3000, 1200],
    'listing_price': [300000, 450000, 350000, 500000, 200000]
})

# 1. Average listing price by location
avg_price_by_location = property_data.groupby('location')['listing_price'].mean()

# 2. Number of properties with more than 4 bedrooms
num_properties_gt_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

# 3. Property with the largest area
largest_area_property = property_data.loc[property_data['area_sqft'].idxmax()]

# Display results
print("1. Average listing price by location:")
print(avg_price_by_location)

print(f"\n2. Number of properties with more than 4 bedrooms: {num_properties_gt_4_bedrooms}")

print("\n3. Property with the largest area:")
print(largest_area_property)
