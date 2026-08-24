# Worldwide Weather Project

A Python command-line application that fetches current weather data for any city worldwide using the OpenWeather API, displays the formatted results, and logs each search into a CSV file.

## Features

- Takes city and country inputs from the user (and US state code if applicable).
- Uses OpenWeather Direct Geocoding API to find geographical coordinates.
- Queries OpenWeather Current Weather API for real-time weather metrics in Celsius.
- Displays the weather details in the terminal.
- Automatically creates and appends search results to a local CSV file.

## Requirements and Setup

Make sure Python 3 is installed on your system.

1. Install the required dependencies:
   pip install -r requirements.txt

2. Configure your API key file:
   The project requires a `.env` file in the root folder to securely load your API key.
   Create a file named `.env` and add your key inside:
   KEY=your_openweather_api_key_here

## Running the Application

Run the main script:
python main.py

Follow the prompts in the terminal:
- Enter a city name (e.g. Jerusalem, New York).
- Enter a 2-letter country code (e.g. IL, US, GB).
- If the country is US, enter a 2-letter state code (e.g. TX).

## Example Run

Enter city: Jerusalem
Enter country code (For example Israel: IL): IL

search_time: 2026-08-24 19:40:00
City: Jerusalem
Country: IL
Temperature: 28.5°C
Feels like: 29.1°C
Condition: clear sky
Humidity: 52%
Wind speed: 3.4 m/s

Weather result saved to weather_history.csv

## Data Storage

All successful queries are stored in weather_history.csv. If the file does not exist, the program creates it and writes the header row automatically without overwriting previous entries.