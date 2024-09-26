# Imports
from google.cloud import storage
import requests
import json
from soadpy import Socrata
import pandas as pd
from io import StringIO


# Create a client object that points to GCS
storage_client = storage.Client()

# Define the bucket
bucket_name = 'my-bigdataproject-jg'
bucket = storage_client.get_bucket(bucket_name)

# Destination folder
destination_folder = 'landing/'

"""
# Read the JSON config file
config_file_path = 'config.json'
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file) 

# Taxi API Authentication
taxi_token  = config['taxi_token']
taxi_username = config['taxi_username']
taxi_password = config['taxi_password'] 
"""

# Taxi Data API URL's
taxi_data_domain = "data.cityofnewyork.us"
taxi_data_ids = {
    "4b4i-vvec" : "2023"
}

def extract_taxi_data(taxi_data_id):
    year = taxi_data_ids[taxi_data_id]
    print(f"Extracting taxi data for year: \t{year}")
    client = Socrata(taxi_data_domain, None)

    tax_records = []
    offset = 0
    limit = 50000

    while True:
        records = client.get(taxi_data_id, limit=limit, offset=offset)
        if not records:
            break
        tax_records.extend(records)
        offset += limit
        print(f"\nFetched {len(tax_records)} records so far...")

    print(f"\nTotal records fetched: {len(tax_records)}")

    print(f"Converting to DataFrame...")
    df = pd.DataFrame.from_records(tax_records)
    
    file_name = f"yellow_taxi_data_{year}.csv"
    csv_buffer = StringIO()
    print(f"Saving to CSV: \t{file_name}")
    df.to_csv(csv_buffer, index=False)
    
    # Upload to GCS
    print(f"Uploading to GCS: \t{file_name}")
    blob = bucket.blob(destination_folder + file_name)
    blob.upload_from_string(csv_buffer.getvalue(), content_type='text/csv')
    
    print(f"Upload complete: \t{file_name}")



# Main function
def main():
    
    # Loop through the taxi data ids keys
    print("Downloading taxi data...")
    for taxi_data_id in taxi_data_ids.keys():
        extract_taxi_data(taxi_data_id)
    
    print("All taxi data uploaded to GCS!")
    
    

if __name__ == "__main__":
    main()
        