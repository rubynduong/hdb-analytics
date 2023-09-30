import pandas as pd 

# Load the raw data and add a new address column 
raw_df = pd.read_csv("data/raw-data.csv",low_memory=False)
raw_df["address"] = raw_df["block"] + " " + raw_df["street_name"] + ", " + raw_df["town"] + ", SINGAPORE"
# Add the flat_location dataset 
flat_location = pd.read_csv("data/flat-location.csv")

# Merge the raw-data with the flat_location data on the address of each flat 
transformed_data = pd.merge(raw_df,flat_location,how="left",on="address")
# transformed_data.drop(columns="Unnamed: 0", inplace=True)


# change to time format for date columns
for x in ['month','lease_commence_date']:
    transformed_data[x] = pd.to_datetime(transformed_data[x]).dt.normalize()

# As the remaining_lease has a lot of null values, we will drop that column
transformed_data.drop(columns='remaining_lease',inplace=True)

# create a remaining lease value
transformed_data["remaining_lease"] = transformed_data["lease_commence_date"].dt.year + 99 -transformed_data["month"].dt.year

# transformed_data.to_csv("data/transformed-data.csv")