# Use OneMapAPI to get the coordinates of MRTs, schools, and malls. 
# API documentation: https://www.onemap.gov.sg/apidocs/apidocs
import pandas as pd 
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor
from mall_list import mall_list


mall_buildings = []
mall_lat=[]
mall_lon = []

def call_mall_api(mall):
    # Construct the query address
    query= "https://www.onemap.gov.sg/api/common/elastic/search?searchVal="+ mall+ "&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    headers = {"Authorization": "**********************"}
    # Invoke a GET request
    response = requests.request("GET", query, headers=headers)
    # Load the content of the request into a Python dictionary  
    mall_content = json.loads(response.content)

    if mall_content["found"] > 0:
        # Get the building name for each MRT station
        mall_buildings_value = mall_content["results"][0]["BUILDING"]
        mall_buildings.append(mall_buildings_value)
        # Get the lat for each MRT station
        mall_lat_value= mall_content["results"][0]["LATITUDE"]
        mall_lat.append(mall_lat_value)
        # Get the lon for each MRT station
        mall_lon_value = mall_content["results"][0]["LONGITUDE"]
        mall_lon.append(mall_lon_value)
        # Print the result for that MRT
        result = print(str(mall) +", Lat: " + mall_lat_value + " , Long: "+mall_lon_value)

    else:
        mall_buildings.append("Not Found")
        mall_lat.append("Not Found")
        mall_lon.append("Not Found")
        result = print("This address was not found")
    return result 


# Call the call_malll_api function 
if __name__ =="__main__":
    start_time= time.time()
    executor = ThreadPoolExecutor(12)

    for mall in mall_list:
        future = executor.submit(call_mall_api,(mall))
        
    print(future.result())
        
    elapsed = time.time() - start_time
    print(f"Elapsed: {elapsed:.2f}s")

# Create a DataFrame for the mall buildings, lat and lon. 
mall_location = pd.DataFrame(
    {
        'Mall Building Name':mall_buildings ,
        "Latitude": mall_lat,
        "Longitude": mall_lon
    }
)

mall_location = mall_location[mall_location["Mall Building Name"].str.contains("Not Found") == False]

# Export the mall location data to a csv file 
mall_location.to_csv("data/mall_location.csv")