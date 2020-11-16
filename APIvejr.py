import requests, datetime


class weatherAPI:
    lastTimeUpdated = datetime.datetime.now()

    def getWeather(self):
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
        differenceInSeconds = (now - weatherAPI().lastTimeUpdated).total_seconds()
        return differenceInSeconds