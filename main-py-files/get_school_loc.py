# Use OneMapAPI to get the coordinates of MRTs, schools, and malls. 
# API documentation: https://www.onemap.gov.sg/apidocs/apidocs
import pandas as pd 
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor
from school_list import school_list


school_buildings = []
school_lat=[]
school_lon = []
def call_school_api(school):
    # Construct the query address
    query= "https://www.onemap.gov.sg/api/common/elastic/search?searchVal="+ school+ "&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    headers = {"Authorization": "**********************"}
    # Invoke a GET request
    response = requests.request("GET", query, headers=headers)
    # Load the content of the request into a Python dictionary  
    school_content = json.loads(response.content)

    if school_content["found"] > 0:
        # Get the building name for each MRT station
        school_buildings_value = school_content["results"][0]["BUILDING"]
        school_buildings.append(school_buildings_value)
        # Get the lat for each MRT station
        school_lat_value= school_content["results"][0]["LATITUDE"]
        school_lat.append(school_lat_value)
        # Get the lon for each MRT station
        school_lon_value = school_content["results"][0]["LONGITUDE"]
        school_lon.append(school_lon_value)
        # Print the result for that MRT
        result = print(str(school) +", Lat: " + school_lat_value + " , Long: "+school_lon_value)

    else:
        school_buildings.append("Not Found")
        school_lat.append("Not Found")
        school_lon.append("Not Found")
        result = print("This address was not found")
    return result 

# Call the call_mrt_api function 
if __name__ =="__main__":
    start_time= time.time()
    executor = ThreadPoolExecutor(100)

    for school in school_list:
        future = executor.submit(call_school_api,(school))
        
    print(future.result())
        
    elapsed = time.time() - start_time
    print(f"Elapsed: {elapsed:.2f}s")

# Create a DataFrame for the school buildings, lat and lon. 
school_location = pd.DataFrame(
    {
        'School Building Name':school_buildings ,
        "Latitude": school_lat,
        "Longitude": school_lon
    }
)

school_location = school_location[school_location["School Building Name"].str.contains("Not Found") == False]

# Export the school location data to a csv file 
school_location.to_csv("data/school_location.csv")