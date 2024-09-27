# Predicting-New-York-City-Taxi-Demand

## Data Sources:
### New York City Taxi and Limousine Commission (TLC) Yellow Taxi Trip Records (~3 GB each file)
2023 Yellow Taxi Trip Data - https://data.cityofnewyork.us/Transportation/2023-Yellow-Taxi-Trip-Data/4b4i-vvec/about_data 

2022 Yellow Taxi Trip Data - https://data.cityofnewyork.us/Transportation/2022-Yellow-Taxi-Trip-Data/qp3b-zxtp/about_data

2021 Yellow Taxi Trip Data - https://data.cityofnewyork.us/Transportation/2021-Yellow-Taxi-Trip-Data/m6nq-qud6/about_data

### Weather Data from Visual Crossing (data size not measured yet)
https://www.visualcrossing.com/weather/weather-data-services

## Data Description:
The NYC Yellow Taxi Trip Data provides general information about taxi trips in New York City. The dataset contains location identifiers for pickup and dropoff points. It also includes fare components, including fare amount, payment type, taxes, surcharges, and tolls. This project will primarily use pickup and drop-off times to analyze historical demand patterns for taxi trips.

The Weather Data from Visual Crossing offers detailed weather data for each day. It includes temperature data like the daily average, min, max and feels like temperature. There is also data on preciptation, snow, winds and humidity. 

## Prediction and Goals:
For this project I attempt to predict daily number of taxi trips in New York City based on historical demand patterns and weather conditions. This can help taxi companies optimize their staff management and improve efficiency 

The variable I will predict will be daily total number of taxi trips, which will be derived by aggregating the individual trip records from the NYC Yellow Taxi Trip Data.

I will be using a linear regression model for this project to identify relationships between weather and taxi demands. 

# Data Acquisition 
Google Cloud Storage:
This project used a virtual machine instance configured as e2-standard-4 with 4 vCPU’s, 16 GB RAM, and a 12 GB storage disk. For cloud storage, the following bucket and folder format was implemented: 


## VM and Python Set Up:
To see which VM commands are needed for this project, refer to the set_up_vm.sh script in /programming_scripts. 

For the Python scripts, we will be working with google.cloud, pandas, and sodapy libraries. For each Python script, you must set up a Google Cloud Storage client and define the bucket and destination folder.

## Extracting Taxi Data:
The complete extracting_taxi_data.py code is in /programming_scripts.

To get the taxi data for each year, NYC Open Data provides a free API endpoint using Socrata (https://dev.socrata.com/foundry/data.cityofnewyork.us/4b4i-vvec). The dataset for each year has an ID, so a dictionary was created to store this information. In the main function, it will loop to get the dataset ID’s from 2021 to 2023 and extract the data one at a time. 

To extract the data for each year, we will use Socrata to request the data. Each request is limited to 50,000 records, so we will combine all the requested data into a data frame. Each dataset has more than 30 million records, and attempting to get all records in the dataset will crash the VM. To compensate for this, the script gets up to 5 million records in a dataset and then uploads it to GCS. Once all the data from the dataset is extracted, it will move on to the following years dataset. 

## Extracting Weather Data:
The complete extracting_weather_data.py code is in /programming_scripts

To retrieve the weather data, we will use Visual Crossing. You must create an account and obtain an API Key (https://www.visualcrossing.com/weather-api). We will retrieve daily weather data for the 5 boroughs from 2021 to 2023. This is a total of about 5,475 records, and free accounts are limited to 1,000 records a day. This script is structured to extract weather data for a single borough and a specific year. 

The program starts by asking you to choose a borough and year from a list. The Visual Crossing API will retrieve weather data based on the location and date range provided(https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/). In the parameters, we specify that daily data should be returned in CSV format. Finally, we process the CSV and save it to GCS.

