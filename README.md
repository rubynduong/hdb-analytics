# HDB Analytics  

## Introduction 

Welcome to the GitHub repository for the project Singapore HDB Price Analysis. This hands-on project involves the end-to-end development of Tableau dashboards to answer the key questions/ requirements:
1. A dashboard to provide a national/regional overview of the number of resale transactions, and median prices across the years from 1990 to 2023.
2. A dashboard to show towns with the largest flats based on users' budget
3. A dashboard to show flats of the best areas based on users' budget


## Data Sources

Resale HDB data: https://beta.data.gov.sg/collections

## Data Collection

Data collection is conducted by running raw_data.py, includes the steps of downloading csv files using wget, concatenating data of all periods, and export into a combined CSV file named raw-data.csv 

## Geocode the flat addresses to prepare for distance calculation to important locations

Geocoding flat addresses is conducted by running get_flat_location.py, using Nominatim from geopy package. 

## Collect geocoded data of important locations to prepare for the distance calculation from flats 

Prepare a list of important locations: mall_list.py, mrt_list.py, school_list.py

Geocoded data of important locations (malls, schools, and MRT stations) are collected by running get_mall_loc.py, get_mrt_loc.py, get_school_loc.py.

## Calculate the distance between flats and malls/schools/MRT stations

This distance calculation is conducted by running distance_data.py and its result is the distance-data.csv file. 

## Data Transformation

Merge the distance data with the raw data by running transform_data.py and exports the result to transformed_data.csv

## Create Tableau dashboards

Create 3 dashboards to answer to the 3 answers/ requirements. 





