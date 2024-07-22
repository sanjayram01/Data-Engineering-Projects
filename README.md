# Weather Data ETL Pipeline

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

