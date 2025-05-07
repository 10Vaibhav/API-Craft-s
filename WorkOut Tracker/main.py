import requests as r
import datetime as dt
import os
from dotenv import load_dotenv
current = dt.datetime.now()

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
Token = os.getenv('TOKEN')
Url = "https://trackapi.nutritionix.com/v2/natural/exercise"

print("Please Enter Valid Exercise !!")
query = input("Tell Me Which Exercise You Did: ")

user_params = {
    "query": query,
    "weight_kg": 75,
    "height_cm": 167.64,
    "age": 21
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = r.post(url=Url, json=user_params, headers=headers)
data = response.json()
# print(data)

exercise_name = data['exercises'][0]['name'].title()
exercise_duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']

# print(exercise_name)
# print(exercise_duration)
# print(calories)

formatted_date = current.strftime('%d/%m/%Y')
# print(formatted_date)

formatted_time = current.strftime('%I:%M %p')
# print(formatted_time)

# print(formatted_time)

sheet_url = os.getenv('SHEET_URL')

body = {
    "workout": {
        # Replace with actual workout data
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": calories
    }
}


headers = {
    "Authorization": Token
}

Entry = r.post(sheet_url, json=body, headers=headers)

entry_response = Entry.json()
print(entry_response['workout'])
