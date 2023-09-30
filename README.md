# HDB Analytics  

## Introduction 

This is the GitHub repository for the data analysis project of Singapore HDB Resale Prices. This project involves the end-to-end development of 3 Tableau dashboards to answer 3 key requirements.

1. The dashboard should  provide a **national/regional overview** of the number of resale transactions, and median prices across the years from 1990 to 2023.

2. Buyers would want to **minimize the distances from the flat to important locations** such as MRT stations, malls, schools. The dashboard should help buyers to select the best location, given buyers' input budgets.

3. Buyers would want to **optimize the flat size within a given budget**. The dashboard should suggest buyers which towns had the largest flats based on historical transactions, given buyers' input budgets. 

Check out the public Tableau dashboards [here](https://public.tableau.com/app/profile/ruby.duong/viz/SingaporeHDBDashboard/Overview)!

## 1. Data Sources

Resale HDB data: https://beta.data.gov.sg/collections


## 2. Data Collection

Data collection is conducted by running `raw_data.py`, includes the steps of downloading csv files using wget, concatenating data of all periods, and export into a combined CSV file named raw-data.csv 

## 3. Data Wrangling

As one of the requirements involve distance data between the flats and important locations, we will geocode the flat addresses and those locations. 

This geocoding task is done by running `get_mall_loc.py`, `get_mrt_loc.py`, `get_school_loc.py`

The script `distance_data.py` calculates the distances from the flats to malls, schools, and MRT stations. 


## 4. Data Transformation

Merge the distance data with the raw data by running `transform_data.py` and exports the result to `transformed_data.csv`


## 5. Visualize data with Tableau to answer 3 key questions

Using the transformed data in `transformed-data.csv`, using Tableau to create corresponding visualization and features to satisfy the 3 requirements. 

1. **Overview**: HDB Resale Median Price & Number of Transactions, which can be filtered by invidual towns, time period, storey ranges, and flat types (1/2/3/4/5 room, executive, multi-generation)

*A snapshot of the dashboard:* 

![Overview](https://github.com/rubynduong/hdb-analytics/assets/106129711/b600053e-0356-460d-aaed-d3bdbe3ae284)

2. **Distance Optimization**: Users input their budgets, desired distances to nearest MRT stations, malls, schools and Raffles MRT Station (CBD), the dashboard will provide the streets and towns that satisfy the requirements. Users can also find streets based on nearest MRT station, malls or schools.

*A snapshot of the dashboard:* 

![Distance Optimization](https://github.com/rubynduong/hdb-analytics/assets/106129711/975dd0ae-3834-4664-8c63-c83e03a08e3d)

3. **Size Optimization**: Users input their budgets and the dashboard provides the size of the biggest flat in each town; as well as the flat average size of the streets.

*A snapshot of the dashboard:* 

![Size Optimization](https://github.com/rubynduong/hdb-analytics/assets/106129711/d1063bf0-e810-4682-9d96-1635000616cf)

