import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from geopy.geocoders import Nominatim
import os

# Read country name from file
with open('model_response.txt', 'r') as file:
    country_name = file.read().strip()

# Get coordinates
geolocator = Nominatim(user_agent="location_plotter")
location = geolocator.geocode(country_name)
lat, lon = location.latitude, location.longitude

# Create output directory
output_dir = "/home/harsh/Location-Predictor"
os.makedirs(output_dir, exist_ok=True)

# Create map
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()
ax.add_feature(cfeature.LAND, facecolor='#e0e0e0')
ax.add_feature(cfeature.OCEAN, facecolor='#9ec9ff')
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)

# Plot simple red dot at location
ax.plot(lon, lat, 'ro', markersize=8, transform=ccrs.PlateCarree())

# Add subtle gridlines
ax.gridlines(color='gray', linestyle='--', alpha=0.5)

# Save output
plt.savefig(f'{output_dir}/world_location.png', dpi=300, bbox_inches='tight')
plt.close()
