# Imports
from google.cloud import storage
import requests


# Create a client object that points to GCS
storage_client = storage.Client()

# Define the bucket
bucket_name = 'my-bigdataproject-jg'
bucket = storage_client.get_bucket(bucket_name)

# Destination folder
destination_folder = 'landing/'

# Taxi Zone URL information
url = "https://data.cityofnewyork.us/api/views/755u-8jsi/rows.csv?accessType=DOWNLOAD"

Headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

session = requests.Session()

def extract_taxi_zones():
    print("Extracting taxi zones...")
    response = session.get(url, headers=Headers)
    print("Found taxi zones.")
    data = response.content
    print("Uploading to GCS...")
    blob = bucket.blob(destination_folder + "taxi_zones.csv")
    blob.upload_from_string(data)
    print("Upload complete.")

if __name__ == "__main__":
    # Loop through the taxi data ids keys
    print("Downloading taxi zones...")
    extract_taxi_zones()
    print("Download complete.")