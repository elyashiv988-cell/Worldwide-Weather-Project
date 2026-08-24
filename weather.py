import csv
import json
import os
import datetime
import time
import requests
import dotenv


def get_key():

    if os.path.exists(".env"):
        dotenv.load_dotenv(".env")
        key = os.getenv("KEY")
        return key

    else:
        print(".env file doesn't found!")

def get_city():

    city = input("Enter city: ")
    city = city.strip().lower()
    if len(city)==0:
        print("City name must contains chars. ")
        exit()
    else:
        return city

def get_country_code():

    country = input("Enter country code (For example Israel: IL.): ")
    country = country.lower().strip()
    if len(country)==2:
        return country
    else:
        print("Country code must contains exactly 2 letters. ")
        exit()


def get_us_code(country):
    
    state = input("Enter state code: (For example Texas: TX.) ")
    state = state.lower().strip()
    if len(state)==2:
        return state
    else:
        print("State code must contains exactly 2 letters. ")
        exit()

def get_location(city_name, country_code, key, state_code=" ", limit=1):

    uml = f"http://api.openweathermap.org/geo/1.0/direct"

    
    start_time = time.time()

    try:
        if country_code == "US":
            state_code = get_us_code()
            response = requests.get(f"{uml}?q={city_name},{state_code},{country_code}&limit={limit}&appid={key}")
        else:
            response = requests.get(f"{uml}?q={city_name},{country_code}&limit={limit}&appid={key}")
        corrent_time = time.time()
        if corrent_time - start_time < 30:
            coordinates = response.json()
            return coordinates[0]["lat"], coordinates[0]["lon"]

    except:
        print("Location not found!")
        exit()


    
