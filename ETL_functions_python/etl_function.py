# %%
#Importing important libraries 

import pandas as pd
import requests
# %%

# Extract Function 

def fetch_weather_data(city: str, api_key: str):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = 'your_openweathermap_api_key'
city = 'London'
weather_data = fetch_weather_data(city, api_key)
print(weather_data)
# %%

# Transformation Function 


def transform_weather_data(data: dict):
    
    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'wind_deg': data['wind']['deg']
    }
    return weather_info


transformed_data = transform_weather_data(weather_data)
print(transformed_data)

# %%

# Load Function 

def load_data_to_csv(data: dict, file_path: str):
    df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)


output_file = 'weather_data.csv' # Replace with your local directory path
load_data_to_csv(transformed_data, output_file)
print(f'Data saved to {output_file}')

# %%
