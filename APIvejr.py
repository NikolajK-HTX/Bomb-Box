import requests
import datetime


class WeatherAPI:
    lastTimeUpdated = datetime.datetime.now()

    def getTemperature(self):
        WeatherAPI.lastTimeUpdated = datetime.datetime.now()

        key = "c59712f4440365ed016958173d3b05cf"
        CITY = "Aarhus"
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        URL = BASE_URL + "q=" + CITY + "&appid=" + key
        response = requests.get(URL)
        data = response.json()
        temperature = round(data['main']['temp']-273.15)
        return temperature

    def timeSinceLastUpdate(self):
        now = datetime.datetime.now()
        differenceInSeconds = (
            now - WeatherAPI.lastTimeUpdated).total_seconds()
        return differenceInSeconds


if __name__ == "__main__":
    import time

    weather = WeatherAPI()
    temperature = weather.getTemperature()
    time.sleep(2)
    difference = weather.timeSinceLastUpdate()
    print('Temperaturen er {} grader celsius'.format(temperature))
    print('Det blev tjekket for {} sekunder siden'.format(difference))
