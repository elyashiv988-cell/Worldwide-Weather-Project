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

    country = input("Enter country code (For example Israel: IL): ")
    country = country.lower().strip()
    if len(country)==2:
        return country
    else:
        print("Country code must contains exactly 2 letters. ")
        exit()

def is_usa(country):
    if country == "US":
        return True

def get_us_code(country):
    
    state = input("Enter state code: (For example Texas: TX) ")
    state = state.lower().strip()
    if len(state)==2:
        return state
    else:
        print("State code must contains exactly 2 letters. ")
        exit()

def get_location(country_code, state_code, city_name, key, limit=1):
 
    base_uml = f"http://api.openweathermap.org/geo/1.0/direct"
    
    
    try:
        start_time = time.time()

        if is_usa(country_code):
            
            response = requests.get(f"{base_uml}?q={city_name},{state_code},{country_code}&limit={limit}&appid={key}")
        else:
            response = requests.get(f"{base_uml}?q={city_name},{country_code}&limit={limit}&appid={key}")

        corrent_time = time.time()

        if corrent_time - start_time < 30:
            coordinates = response.json()
            return coordinates
        else: 
            print("TIme over!")
            exit()

    except:
        print("Location not found!")
        exit()

def get_weather(latitude, longitude, key):

    base_uml = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(f"{base_uml}?lat={latitude}&lon={longitude}&units=metric&appid={key}")
    weather_data= response.json()

    return weather_data

def process_weather_data(location, weather):
    data_dict = {}
    #data_dict["search_time"] = None
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

    print(f"City: {weather_result["city"]}")

    if weather_result["state"].strip()!="":
        print(f"State: {weather_result["state"]}")

    print(f"Country: {weather_result["country"]}\nTemperature: {weather_result["temperature"]}\nFeels like: {weather_result["feels_like"]}\nCondition: {weather_result["condition"]}\nHumidity: {weather_result["humidity"]}\nWind speed: {weather_result["wind_speed"]}")

def save_weather_to_csv(weather_result):

    data = weather_result
    headers=["city","state", "country", "temperature", "feels_like", "condition", "humidity", "wind_speed"]

    with open("weather_history.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        if os.path.getsize("weather_history.csv") ==0:
            writer.writeheader()
        writer.writerow(data)




    



                    
                    
                    
                    
                    
                    
    


    

    
