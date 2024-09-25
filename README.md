# Predicting-New-York-City-Taxi-Demand

## Data Sources:
New York City Taxi and Limousine Commission (TLC) Yellow Taxi Trip Records (~3 GB each file)

2023 Yellow Taxi Trip Data  
2022 Yellow Taxi Trip Data  
2021 Yellow Taxi Trip Data 

Weather Data from Visual Crossing (data size not measured yet)

https://www.visualcrossing.com/weather/weather-data-services

## Data Description:
The NYC Yellow Taxi Trip Data provides general information about taxi trips in New York City. The dataset contains location identifiers for pickup and dropoff points. It also includes fare components, including fare amount, payment type, taxes, surcharges, and tolls. This project will primarily use pickup and drop-off times to analyze historical demand patterns for taxi trips.

The Weather Data from Visual Crossing offers detailed weather data for each day. It includes temperature data like the daily average, min, max and feels like temperature. There is also data on preciptation, snow, winds and humidity. 

## Prediction and Goals:
For this project I attempt to predict daily number of taxi trips in New York City based on historical demand patterns and weather conditions. This can help taxi companies optimize their staff management and improve efficiency 

The variable I will predict will be daily total number of taxi trips, which will be derived by aggregating the individual trip records from the NYC Yellow Taxi Trip Data.

I will be using a linear regression model for this project to identify relationships between weather and taxi demands. 
