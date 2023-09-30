# HDB Analytics  

## Introduction 

Welcome to the GitHub repository for the data analysis project of Singapore HDB Resale Prices. This hands-on project involves the end-to-end development of Tableau dashboards to answer 3 key questions/ requirements.

1. This dashboard should  provide a **national/regional overview** of the number of resale transactions, and median prices across the years from 1990 to 2023.

2. Buyers would want to **minimize the distances from the flat to important locations** such as MRT stations, malls, schools. This dashboard should help buyers to select the best location, given buyers' input budgets.

3. Buyers would want to **optimize the flat size within a given budget**. This dashboard should suggest buyers which towns had the largest flats based on historical transactions, given buyers' input budgets. 

## Data Sources

Resale HDB data: https://beta.data.gov.sg/collections

## Data Collection

Data collection is conducted by running `raw_data.py`, includes the steps of downloading csv files using wget, concatenating data of all periods, and export into a combined CSV file named raw-data.csv 

## Geocoding the flat addresses 

Geocoding flat addresses is conducted by running `get_flat_location.py`, using Nominatim from geopy package. 

## Collecting geocoded data of important locations: malls, MRT stations, schools 

Prepare a list of important locations: `mall_list.py`, `mrt_list.py`, `school_list.py`

Geocoded data of important locations (malls, schools, and MRT stations) are collected by running `get_mall_loc.py`, `get_mrt_loc.py`, `get_school_loc.py`.

## Calculate the distance between flats and malls/schools/MRT stations

This distance calculation is conducted by running `distance_data.py` and its result is the `distance-data.csv` file. 

## Data Transformation

Merge the distance data with the raw data by running `transform_data.py` and exports the result to `transformed_data.csv`

## Create Tableau dashboards

Using the transformed data in `transformed-data.csv`, using Tableau to create corresponding visualization and features to satisfy the 3 requirements. 

1. Overview: HDB Resale Median Price & Number of Transactions, which can be filtered by invidual towns, time period, storey ranges, and flat types (1/2/3/4/5 room, executive, multi-generation)

![Overview](https://github.com/rubynduong/hdb-analytics/assets/106129711/b600053e-0356-460d-aaed-d3bdbe3ae284)

2. Distance Optimization: Users input their budgets, desired distances to nearest MRT stations, malls, schools and Raffles MRT Station (CBD), the dashboard will provide the streets and towns that satisfy the requirements. Users can also find streets based on nearest MRT station, malls or schools.

![Distance Optimization](https://github.com/rubynduong/hdb-analytics/assets/106129711/975dd0ae-3834-4664-8c63-c83e03a08e3d)

3. Size Optimization: Users input their budgets and the dashboard provides the size of the biggest flat in each town; as well as the flat average size of the streets.

![Size Optimization](https://github.com/rubynduong/hdb-analytics/assets/106129711/d1063bf0-e810-4682-9d96-1635000616cf)





[`HDB_resale.csv`]('HDB_resale.csv')