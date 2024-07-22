# Weather Data ETL Pipeline using Python

This repository contains a simple ETL (Extract, Transform, Load) pipeline built in Python. The pipeline fetches weather data from the OpenWeatherMap API, transforms the data into a structured format, and loads it into a CSV file.

## Introduction
ETL (Extract, Transform, Load) is a fundamental process in data engineering, enabling the collection, transformation, and storage of data from various sources. This project demonstrates how to build a simple ETL pipeline in Python that fetches weather data from an API, transforms it, and stores it in a CSV file.

## Setup
To get started, you’ll need Python 3.8+ and the following libraries installed:

```
pip install requests pandas
```

You will also need an API key from OpenWeatherMap. Follow these steps to obtain your API key:

Sign up for a free account on the OpenWeatherMap website.
Navigate to the Current Weather Data section and get your API key.

## Usage
Replace your_openweathermap_api_key with your actual OpenWeatherMap API key in the script.

Running the Script
To run the script, execute the following command in your terminal:

```
python weather_etl.py
```
## Flow

1.Extract:

Fetch weather data using the OpenWeatherMap API.
Example function: fetch_weather_data

2.Transform:

Transform the fetched weather data into a structured format.
Example function: transform_weather_data

3.Load:

Load the transformed data into a CSV file.
Example function: load_data_to_csv

4.Complete Pipeline:

Integrate all steps in the main function.
Fetch, transform, and load the data when the script is run.

## Medium Post
For a detailed guide on building this ETL pipeline, refer to my Medium post:

https://medium.com/@sanjayramrajasrinivasan/building-a-simple-etl-pipeline-in-python-a-beginners-guide-d2ab9204e207

## Conclusion
In this tutorial, we built a simple ETL pipeline in Python that fetches data from an API, transforms it, and saves it to a CSV file. This project helps you understand the ETL process, which is crucial in data engineering and analytics.
