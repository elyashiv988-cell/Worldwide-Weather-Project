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

