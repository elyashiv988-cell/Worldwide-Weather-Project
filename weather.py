import csv
import json
import os
import datetime
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
