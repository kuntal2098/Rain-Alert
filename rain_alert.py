import requests
from twilio.rest import Client

API_KEY = '<OpenWeathermap API Key>'
MY_LAT, MY_LONG = '<Latitude of your location>', '<Longitude of your location>'
TWILIO_ACC_SID = '<Twilio Account ID>'
TWILIO_AUTH_TOKEN = '<Twilio Authentication Token>' #For SMS Service, you need to setup an account in Twilio.com from where you will get SID along with an access token and a number
PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "minutely,daily,current",
    "appid": API_KEY
}
#This code uses information provided by an API service from Openwaethermap.org
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=PARAMS)
context = response.json()["hourly"][:12]

will_rain = False
for i in context:
    if i["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body="It's gonna rain today. Take your umbrella",
        from_='<The number you will get once you setup an account in Twilio>',
        to='<Your Number along with country code>'
    )

    print(message.status)

