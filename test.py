key = "c59712f4440365ed016958173d3b05cf"
import requests
CITY = "Aarhus"
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

URL = BASE_URL + "q=" + CITY + "&appid=" + key

response = requests.get(URL)


data = response.json()
main = data['main']
temperature = main['temp']
humidity = main['humidity']
pressure = main['pressure']
report = data['weather']
print(f"{CITY:-^30}")
print(f"Temperature: {temperature-273.15}")
print(f"Humidity: {humidity}")
print(f"Pressure: {pressure}")
print(f"Weather Report: {report[0]['description']}")
