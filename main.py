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
from buzzer import BuzzerCountdown
import string
import random


# Set the duration of the game in minutes
gameDuration = 2
timeGameStarted = time.time()

vejr = WeatherAPI()
temperatur = vejr.getTemperature()
print("Temperaturen er {} grader.".format(temperatur))

led1 = LED(2) # led connected to D2

button1 = button(4) # button connected to D4
button1Timer = Timer(2) # hold down button in 2 seconds
buttonPressed = False

buzzer = BuzzerCountdown(6, gameDuration, 5)

serialNumber = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
serialNumber += random.choice(string.digits)
print("Serienummeret er {}".format(serialNumber))

display.setText("Temp: {} \n#{}".format(temperatur, serialNumber))
display.setRGB(255, 0, 0)

buttonDefused = False

won = False

while True:
    # opdater temperaturen hvert andet minut
    if vejr.timeSinceLastUpdate() > 120:
        temperatur = vejr.getTemperature()
        print("Temperaturen er {} grader.".format(temperatur))

    buzzer.on()

    if buttonDefused == False:
        led1.on(1)

    if button1.buttonCheck() and button1Timer.isDone():
        if not buttonPressed:
            print("Du trykkede på knappen")
            button1Timer.start()
            buttonPressed = True
        elif buttonPressed and button1Timer.started:
            button1Timer.stop()
            print("Du holdte knappen nede i 2 sekunder!")
            buttonDefused = True
            won = True
            break
    if not button1.buttonCheck() and buttonPressed:
        button1Timer.stop()
        buttonPressed = False
        print("Du trykker ikke længere på knappen")

    if time.time() - timeGameStarted >= gameDuration*60:
        won = False
        break

    # ellers overarbejder processoren
    time.sleep(0.001)

buzzer.off()
led1.off()

if won:
    print("Du har vundet")
    display.setText("BOMB DEFUSED")
else:
    print("Du har tabt")
    display.setText("BOMB EXPLODED")
