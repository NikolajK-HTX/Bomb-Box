# encoding=utf-8
import os
import datetime
import time
if os.name != "nt":  # importeres kun hvis programmet ikke køres på windows
    import grovepi
from APIvejr import WeatherAPI
import display
from button import button
from LED import LED, Timer
from magnetic_switch import MagneticSwitch
import string
import random


vejr = WeatherAPI()
temperatur = vejr.getTemperature()
print("Temperaturen er {} grader.".format(temperatur))

# første led på D1
led1 = LED(2)
button1 = button(4)
button1Timer = Timer(2)
buttonPressed = False
serialNumber = "".join(random.choices(string.ascii_uppercase + string.digits, k=6)) + random.choice(string.digits)
print(serialNumber)


while True:
    # opdater temperaturen hvert andet minut
    if vejr.timeSinceLastUpdate() > 120:
        temperatur = vejr.getTemperature()
        print("Temperaturen er {} grader.".format(temperatur))

    led1.on(1)
    if button1.buttonCheck() and button1Timer.isDone():
        if not buttonPressed:
            print("Du trykkede på knappen")
            button1Timer.start()
            buttonPressed = True
        elif buttonPressed and button1Timer.started:
            button1Timer.stop()
            print("Du holdte knappen nede i 2 sekunder!")
    if not button1.buttonCheck() and buttonPressed:
        button1Timer.stop()
        buttonPressed = False
        print("Du trykker ikke længere på knappen")

    # ellers overarbejder processoren
    time.sleep(0.01)
