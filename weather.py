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
