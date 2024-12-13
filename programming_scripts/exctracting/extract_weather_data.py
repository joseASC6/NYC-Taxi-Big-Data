from google.cloud import storage
import pandas as pd
from io import StringIO
from datetime import datetime
import requests

# Create a client object that points to GCS
storage_client = storage.Client()

# Define the bucket
bucket_name = 'my-bigdataproject-jg'
bucket = storage_client.get_bucket(bucket_name)

# Destination folder
destination_folder = 'landing/'

# Weather API Request URL example:
# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY 

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
years = [2021, 2022, 2023]
key = "" # Replace with your own API key
params = {
    "key" : key,
    "contentType" : "csv",
    "include" : "days"
}

def extract_weather_data(borough, year):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    location = f"{borough}, NY"

    url = f"{base_url}{location}/{start_date}/{end_date}"
    response = requests.get(url, params=params)

    if response.status_code == 200:
        df = pd.read_csv(StringIO(response.text))
        file_name = f"weather_data_{borough}_{year}.csv"
        print(f"Saving to CSV: \t{file_name}")
        csv_buffer = df.to_csv(index=False)
        blob = bucket.blob(destination_folder + file_name)
        blob.upload_from_string(csv_buffer, content_type='text/csv')
        print(f"Upload complete: \t{file_name}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    print("Choose a borough:")
    for i, borough in enumerate(boroughs):
        print(f"{i+1}. {borough}")
    borough = int(input("Select a borough:\t")) - 1

    print("Choose a year:")
    for i, year in enumerate(years):
        print(f"{i+1}. {year}")
    year = int(input("Select the year:\t")) - 1

    borough = boroughs[borough]
    year = years[year]

    print(f"Extracting weather data for {borough} in {year}")

    extract_weather_data(borough, year)