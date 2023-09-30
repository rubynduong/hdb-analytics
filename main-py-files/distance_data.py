
from geopy.distance import geodesic 
import pandas as pd
from geopy.distance import geodesic, great_circle


school_location = pd.read_csv("data/school_location.csv")
school_location.drop(columns="Unnamed: 0",inplace=True)
school_location.rename(columns={"School Building Name":"Building"}, inplace=True)

mrt_location = pd.read_csv("data/mrt_location.csv")
mrt_location.drop(columns="Unnamed: 0",inplace=True)

mall_location = pd.read_csv("mall_location.csv")
mall_location.drop(columns="Unnamed: 0",inplace=True)
mall_location.rename(columns={"Mall Building Name":"Building"}, inplace=True)

flat_location = pd.read_csv("data/flat-location.csv")
flat_location.drop(columns="Unnamed: 0",inplace=True)

# Write for loops to find the nearest school, mrt, mall, the distances to the nearest school, mrt, mall and Raffles MRT 
address = []
d_school = []
n_school = []
d_mrt= []
n_mrt = []
d_mall = []
n_mall = []
d_cbd = []

for add,lat,lon in zip(flat_location.address,flat_location.Latitude,flat_location.Longitude):
    d_to_school = 99
    d_to_mrt = 99
    d_to_mall = 99
    temp = 0

    d_to_cbd = geodesic((lat,lon),(1.345515,103.938437)).km
    d_cbd.append(d_to_cbd)
     
    #loop for schools, MRT and Mall to find the shortest distance to address
    for school,school_lat,school_lon in zip(school_location.Building, school_location.Latitude, school_location.Longitude):
        temp = great_circle((lat, lon), (school_lat, school_lon)).km
        if temp < d_to_school:
            d_to_school = temp
            n_to_school = school
    address.append(add)
    d_school.append(d_to_school)
    n_school.append(n_to_school)

    for mrt,mrt_lat,mrt_lon in zip(mrt_location.MRT, mrt_location.Latitude, mrt_location.Longitude):
        temp = great_circle((lat, lon), (mrt_lat, mrt_lon)).km
        if temp < d_to_mrt:
            d_to_mrt = temp
            n_to_mrt = mrt
    d_mrt.append(d_to_mrt)
    n_mrt.append(n_to_mrt)

    for mall,mall_lat,mall_lon in zip(mall_location.Building, mall_location.Latitude, mall_location.Longitude):
        temp = great_circle((lat, lon), (mall_lat, mall_lon)).km
        if temp < d_to_mall:
            d_to_mall = temp
            n_to_mall = mall
    d_mall.append(d_to_mall)
    n_mall.append(n_to_mall)

# Add new columns into the flat_location dataset 
flat_location["Dist to Nearest School"] = d_school
flat_location["Nearest School"] = n_school
flat_location["Dist to Nearest MRT"] = d_mrt
flat_location["Nearest MRT"] = n_mrt
flat_location["Dist to Nearest Mall"] = d_mall
flat_location["Nearest Mall"] = n_mall
flat_location["Dist to CBD"] = d_cbd
# Export this flat_location to a csv file named distance-data.csv
flat_location.to_csv("data/distance-data.csv")

