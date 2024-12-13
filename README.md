# Project Overview

## Description:
The project analyzes and predicts the tipping behavior of New York City taxi riders using historical trip data and weather conditions. The goal is to explore how external factors, such as weather, time of day, and trip characteristics, influence this tipping behavior. This analysis will help identify patterns in customer behavior and provide actionable insights for stakeholders like the Taxi and Limousine Commission (TLC). 

## Data Sources:
###New York City Taxi and Limousine Commission (TLC) Yellow Taxi Trip Records 
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page 
### Weather Data from Visual Crossing
https://www.visualcrossing.com/weather/weather-data-services

## Data Description:
The NYC Yellow Taxi Trip Data provides general information about taxi trips in New York City. The dataset contains location identifiers for pickup and dropoff points. It also includes fare components, including fare amount, payment type, taxes, surcharges, and tolls. 

The Weather Data from Visual Crossing offers detailed weather data for each day. It includes temperature data like the daily average, min, max, and feels like temperature. There is also data on precipitation, snow, winds, and humidity. 

## Models:
This project develops a Logistic Regression model to predict whether a tip will be "good" (≥15%) or "bad" (<15%) based on various input features. The model uses Logistic Regression, and the evaluation metrics include AUC (Area Under Curve), accuracy, precision, recall, and F1 score.


