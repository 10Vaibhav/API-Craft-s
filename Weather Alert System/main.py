import requests
from twilio.rest import Client

api_key = ""  # OWM_API_KEY
OWM_EndPoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = ""  # TWILIO_ACCOUNT_SID
auth_token = " "  # TWILIO_AUTH_TOKEN

parameters = {

    "lat": 0,  # replace your latitude
    "lon": 0,  # replace your longitude
    "cnt": 4,
    "appid": "472f1602b959e5e1aeb8c58f0c94f80f",
}

response = requests.get(OWM_EndPoint, params=parameters)
response.raise_for_status()

print(response)

data = response.json()

will_rain = False
for i in range(len(data["list"])):
    id_status = data["list"][i]["weather"][0]["id"]
    if id_status < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='',  # TWILIO_FROM_NUMBER
        body="It's going to rain today. Remember to bring an ☔.",
        to=''  # TWILIO_TO_NUMBER
    )
    print(message.status)