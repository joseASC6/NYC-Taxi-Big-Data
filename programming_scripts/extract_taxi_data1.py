# Imports
from google.cloud import storage
import pandas as pd
from io import StringIO
import requests


# Create a client object that points to GCS
storage_client = storage.Client()

# Define the bucket
bucket_name = 'my-bigdataproject-jg'
bucket = storage_client.get_bucket(bucket_name)

# Destination folder
destination_folder = 'landing/'

# Taxi Data URL information
taxi_data_base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
data_years = [2021, 2022, 2023]
#Practice with one year
data_years = [2023]
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

Headers = {{'user-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}}
session = requests.Session()


def extract_taxi_data(file_name):
    print(f"Extracting file: \t{file_name}")
    full_url = taxi_data_base_url + file_name
    response = session.get(full_url, headers=Headers)
    print(f"Found file: \t{file_name}")
    data = response.content
    print(f"Uploading to GCS: \t{file_name}")
    blob = bucket.blob(destination_folder + file_name)
    blob.upload_from_string(data)
    print(f"Upload complete: \t{file_name}")

    
  

if __name__ == "__main__":
    # Loop through the taxi data ids keys
    print("Downloading taxi data...")
    for year in data_years:
        for month in months:
            file_name = f"yellow_tripdata_{year}-{month}.parquet"
            extract_taxi_data(file_name)
    print("Download complete.")
            

