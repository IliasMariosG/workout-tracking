import os
import requests
from constants import URL_NUTRITIONIX, QUESTION
from config import LOAD_DOTENV

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
print(res_from_nutrix)
