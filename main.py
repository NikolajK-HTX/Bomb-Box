from APIvejr import weatherAPI
import os
import datetime
import time
if os.name != "nt":  # importeres kun hvis programmet ikke køres på windows
    import grovepi
import display


vejr = weatherAPI()
temperatur = vejr.getTemperature()
print("Temperaturen er {} grader.".format(temperatur))


while True:
    # opdater temperaturen hvert andet minut
    if vejr.timeSinceLastUpdate() > 120:
        temperatur = vejr.getTemperature()
        print("Temperaturen er {} grader.".format(temperatur))

    time.sleep(0.01)