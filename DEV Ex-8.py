import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 1. Sample data
world_data = pd.DataFrame({
    'Country': ['United States of America', 'Canada', 'India', 'Brazil', 'China'],
    'Value': [100, 150, 200, 80, 120]
})

india_states_data = pd.DataFrame({
    'State': ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Uttar Pradesh', 'Gujarat'],
    'Value': [50, 75, 60, 40, 30]
})

india_districts_data = pd.DataFrame({
    'District': ['Mumbai', 'Bengaluru', 'Chennai', 'Lucknow', 'Ahmedabad'],
    'Value': [20, 30, 25, 15, 10]
})

# 2. Load world map directly from Natural Earth (no deprecated call)
world_map_url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
world_map = gpd.read_file(world_map_url)

# 3. Merge with world data
world_data_geo = world_map.merge(world_data, how='left', left_on='NAME', right_on='Country')

# 4. Create mock India geometry for states and districts
india_geom = world_data_geo[world_data_geo['NAME'] == 'India'].geometry.values[0]

# Duplicate India's shape for demo purposes
india_states_map = gpd.GeoDataFrame(india_states_data.copy(), geometry=[india_geom] * len(india_states_data), crs=world_map.crs)
india_districts_map = gpd.GeoDataFrame(india_districts_data.copy(), geometry=[india_geom] * len(india_districts_data), crs=world_map.crs)

# 5. Plot
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# --- Plot 1: World Data ---
axs[0].set_title("World Data")
world_data_geo.boundary.plot(ax=axs[0], linewidth=0.5)
world_data_geo.plot(column='Value', ax=axs[0], legend=True, legend_kwds={'label': "Values by Country"})

# --- Plot 2: India State Data ---
axs[1].set_title("India States Data")
india_states_map.boundary.plot(ax=axs[1], linewidth=0.5)
india_states_map.plot(column='Value', ax=axs[1], legend=True, legend_kwds={'label': "Values by State"})

# --- Plot 3: India District Data ---
axs[2].set_title("India Districts Data")
india_districts_map.boundary.plot(ax=axs[2], linewidth=0.5)
india_districts_map.plot(column='Value', ax=axs[2], legend=True, legend_kwds={'label': "Values by District"})

plt.tight_layout()
plt.show()
