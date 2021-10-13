import os
import requests
from constants import URL_NUTRITIONIX, QUESTION
from config import LOAD_DOTENV
import datetime

def get_headers():
  return {
    "x-app-id":os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_API_KEY"),
    "Content-type": "application/json"
  }

# print the exercise stats for a plain text input.
def get_input():
  return input(QUESTION)

def get_params_nutrition():
  return {
    "query" : get_input()
  }

# Solution
res = requests.post(url=URL_NUTRITIONIX, json=get_params_nutrition(), headers=get_headers())
res.raise_for_status()
res_from_nutrix = res.json()

# Save data into google sheet
day_month_year_string = datetime.datetime.now().strftime("%d/%m/%Y")
hour_minutes_seconds_microseconds_string = datetime.datetime.now().strftime("%H:%M:%S")

for exercise in res_from_nutrix["exercises"]:
  params_sheety = {
      "workout" : {
        "date" : day_month_year_string,
        "time": hour_minutes_seconds_microseconds_string,
        "exercise" : exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories" : exercise["nf_calories"]
      } 
    }
sheet_response = requests.post(os.environ.get("URL_SHEETY"), json=params_sheety, auth=(os.environ.get("SHEETY_USERNAME"), os.environ.get("SHEETY_PASSWORD")))
print(sheet_response.text)
