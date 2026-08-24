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
    if city.isalpha():
        return city
    else:
        print("Name city can not contains nums!")
        exit()

def get_country_code():

    country = input("Enter country code (For example Israel: IL): ")
    country = country.lower().strip()
    if len(country)==2 and country.isalpha():
        return country
    else:
        print("Country code must contains exactly 2 letters. ")
        exit()

def get_us_code():

    state = input("Enter state code: (For example Texas: TX) ")
    state = state.lower().strip()
    if len(state) == 2 and state.isalpha():
        return state
    else:
        print("State code must contains exactly 2 letters. ")
        exit()

def get_location(country_code, city_name, key, limit=1):
 
    base_uml = f"http://api.openweathermap.org/geo/1.0/direct"

    if country_code == "US":
        state_code = get_us_code()
    else:
        state_code = ""
    
    response = requests.get(f"{base_uml}?q={city_name},{state_code},{country_code}&limit={limit}&appid={key}")
    coordinates = response.json()

    if len(coordinates)==0:
        print("Location not found!")
        exit()
    else:
        return coordinates

def get_weather(latitude, longitude, key):

    base_uml = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(f"{base_uml}?lat={latitude}&lon={longitude}&units=metric&appid={key}")
    weather_data= response.json()
    
    return weather_data

def process_weather_data(location, weather):
    data_dict = {}
    data_dict["search_time"] =datetime.datetime.now()
    data_dict["city"] = location[0]["name"]
    data_dict["state"] = location[0]["state"]
    data_dict["country"] = location[0]["country"]
    data_dict["temperature"] = int(weather["main"]["temp"])
    data_dict["feels_like"] = int(weather["main"]["feels_like"])
    data_dict["condition"] = weather["weather"][0]["description"]
    data_dict["humidity"] = int(weather ["main"]["humidity"])
    data_dict["wind_speed"] = int(weather["wind"]["speed"])
    return data_dict

def print_weather(weather_result):

    print(f"search_time: {weather_result["search_time"]}\nCity: {weather_result["city"]}")

    if weather_result["state"].strip()!="":
        print(f"State: {weather_result["state"]}")

    print(f"Country: {weather_result["country"]}\nTemperature: {weather_result["temperature"]}\nFeels like: {weather_result["feels_like"]}\nCondition: {weather_result["condition"]}\nHumidity: {weather_result["humidity"]}\nWind speed: {weather_result["wind_speed"]}")

def save_weather_to_csv(weather_result):

    headers=["search_time","city","state", "country", "temperature", "feels_like", "condition", "humidity", "wind_speed"]

    with open("weather_history.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        if os.path.getsize("weather_history.csv") ==0:
            writer.writeheader()
        writer.writerow(weather_result)
        print("Weather result saved to weather_history.csv")
        return True
    




    



                    
                    
                    
                    
                    
                    
    


    

    
