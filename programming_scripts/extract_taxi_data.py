# Imports
from google.cloud import storage
from sodapy import Socrata
import pandas as pd
from io import StringIO


# Create a client object that points to GCS
storage_client = storage.Client()

# Define the bucket
bucket_name = 'my-bigdataproject-jg'
bucket = storage_client.get_bucket(bucket_name)

# Destination folder
destination_folder = 'landing/'

# Taxi Data API URL's
taxi_data_domain = "data.cityofnewyork.us"
taxi_data_ids = {
    "4b4i-vvec" : "2023"
}

def upload_to_gcs(taxi_data_year, data, file_number):
    file_name = f"yellow_taxi_data_{taxi_data_year}_{file_number}.csv"
    csv_buffer = StringIO()
    print(f"Saving to CSV: \t{file_name}")
    data.to_csv(csv_buffer, index=False)
    
    # Upload to GCS
    print(f"Uploading to GCS: \t{file_name}")
    blob = bucket.blob(destination_folder + file_name)
    blob.upload_from_string(csv_buffer.getvalue(), content_type='text/csv')
    
    print(f"Upload complete: \t{file_name}")


def extract_taxi_data(taxi_data_id):
    taxi_data_year = taxi_data_ids[taxi_data_id]
    print(f"Extracting taxi data for year: \t{taxi_data_year}")
    client = Socrata(taxi_data_domain, None)

    tax_records = []
    offset = 0 
    limit = 50000
    records_per_file = 1000000 # Number of records per file, change based on RAM capacity
    file_number = 1
    current_records = 0

    while True:
        records = client.get(taxi_data_id, limit=limit, offset=offset)
        if not records:
            break
        tax_records.extend(records)
        current_records += len(records)

        # If we have accumalted enough records, save to GCS
        if current_records >= records_per_file:
            df = pd.DataFrame.from_records(tax_records)
            upload_to_gcs(taxi_data_year, df, file_number)
            

            # Reset the records
            tax_records = []
            current_records = 0
            file_number += 1
    
        offset += limit
        print(f"\nFetched {len(tax_records)} records so far...")

    # Save the remaining records
    if tax_records:
        df = pd.DataFrame.from_records(tax_records)
        upload_to_gcs(taxi_data_year, df, file_number)

    print(f"\nTotal records fetched: {len(tax_records)}")



# Main function
def main():
    
    # Loop through the taxi data ids keys
    print("Downloading taxi data...")
    for taxi_data_id in taxi_data_ids.keys():
        extract_taxi_data(taxi_data_id)
    
    print("All taxi data uploaded to GCS!")
    
    

if __name__ == "__main__":
    main()
        