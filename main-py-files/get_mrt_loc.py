# Use OneMapAPI to get the coordinates of MRTs, schools, and malls. 
# API documentation: https://www.onemap.gov.sg/apidocs/apidocs
import pandas as pd 
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor
from mrt_list import mrt_list


mrt_buildings = []
mrt_lat=[]
mrt_lon = []

def call_mrt_api(mrt):
    # Construct the query address
    query= "https://www.onemap.gov.sg/api/common/elastic/search?searchVal="+mrt+ "&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    headers = {"Authorization": "**********************"}
    # Invoke a GET request
    response = requests.request("GET", query, headers=headers)
    # Load the content of the request into a Python dictionary  
    mrt_content = json.loads(response.content)

    if mrt_content["found"] > 0:
        # Get the building name for each MRT station
        mrt_building_name = mrt_content["results"][0]["BUILDING"]
        mrt_buildings.append(mrt_building_name)
        # Get the lat for each MRT station
        mrt_lat_value= mrt_content["results"][0]["LATITUDE"]
        mrt_lat.append(mrt_lat_value)
        # Get the lon for each MRT station
        mrt_lon_value = mrt_content["results"][0]["LONGITUDE"]
        mrt_lon.append(mrt_lon_value)
        # Print the result for that MRT
        print(str(mrt) +", Lat: " + mrt_lat_value + " , Long: "+mrt_lon_value)

    else:
        mrt_buildings.append("Not Found")
        mrt_lat.append("Not Found")
        mrt_lon.append("Not Found")
        print("This address was not found")
    pass 

# Call the call_mrt_api function 
if __name__ =="__main__":
    start_time= time.time()
    executor = ThreadPoolExecutor(12)

    for mrt in mrt_list:
        future = executor.submit(call_mrt_api,(mrt))
        
    print(future.result())
        
    elapsed = time.time() - start_time
    print(f"Elapsed: {elapsed:.2f}s")

# Create a DataFrame for the MRT buildings, lat and lon. 
mrt_location = pd.DataFrame(
    {
        'MRT': mrt_list ,
        'MRT Building Name':mrt_buildings ,
        "Latitude": mrt_lat,
        "Longitude": mrt_lon
    }
)
# Export the MRT location data to a csv file 
mrt_location.to_csv("data/mrt_location.csv")