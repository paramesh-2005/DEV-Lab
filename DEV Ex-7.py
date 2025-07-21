import pandas as pd
import numpy as np
import folium

# --------------------------
# STEP 1: Generate random data
# --------------------------
np.random.seed(42)
num_points = 100
latitude = np.random.uniform(37.5, 38.5, num_points)
longitude = np.random.uniform(-123, -121, num_points)
value = np.random.randint(1, 100, num_points)

# Create a DataFrame
df = pd.DataFrame({
    'Latitude': latitude,
    'Longitude': longitude,
    'Value': value
})

# Save the DataFrame to a CSV file
df.to_csv('map_data.csv', index=False)

# --------------------------
# STEP 2: Load CSV and analyze
# --------------------------
df = pd.read_csv('map_data.csv')

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# --------------------------
# STEP 3: Create a base map
# --------------------------
base_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()],
                      zoom_start=10)

# Add data points as markers
for index, row in df.iterrows():
    popup_text = f"Value: {row['Value']}"
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=popup_text).add_to(base_map)

# Save the map as an HTML file
base_map.save('interactive_map.html')

print("Interactive map saved as 'interactive_map.html'")
