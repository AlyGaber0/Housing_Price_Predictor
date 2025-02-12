# Main file to write our code
import pandas as pd

first_ottawa_housing = pd.read_csv('ottawa-realestate-data(ottawa-realestate-data).csv')
second_ottawa_housing = pd.read_csv('ca_real_estate.csv')

#filter code to only show ottawa houses
filtered_df = second_ottawa_housing[second_ottawa_housing\
    ['City'].str.contains('Ottawa', case=False, na=False)]

print(filtered_df)