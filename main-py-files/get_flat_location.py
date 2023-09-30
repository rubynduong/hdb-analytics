import pandas as pd
from geopy.geocoders import Nominatim

# Load the raw-data csv file and create a new column for full address 
df = pd.read_csv("data/raw-data.csv")
df["address"] = df["block"] + " " + df["street_name"] + ", " + df["town"] + ", SINGAPORE"

# Dedup Address List and create a list 
df_dedup = df.drop_duplicates(subset='address', keep='first')

address_list = df_dedup['address'].tolist()

# Use Nominatim to geocode the addresses 
geolocator = Nominatim(user_agent="GoogleV3")

address = []
full_address = []
latitude = []
longitude = []
no_result = []


for row in range(len(address_list)):
    #formulate query string 
    try:
        add, (lat, lon) = geolocator.geocode(address_list[row])
        address.append(address_list[row])
        full_address.append(add)
        latitude.append(lat)
        longitude.append(lon)
    except:
        no_result.append(address_list[row])

# Create a DataFrame for the flat address lat and lon. 
df_coordinates = pd.DataFrame({
    'address': address,
    'full_address': full_address,
    'Latitude': latitude,
    'Longitude': longitude
})
# Export the flat location data to a csv file 

df_coordinates.to_csv("data/flat-location.csv")