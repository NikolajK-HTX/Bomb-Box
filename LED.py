import time
from grovepi import *
import random
import datetime


class LED():
    def __init__(self, pin):
        self.led = pin
        pinMode(self.led, "OUTPUT")
        self.timer = Timer(0.5)
        self.blinkState = 0

    def on(self, type):
        if type == 0:
            try:
                digitalWrite(self.led, 1)  # Send HIGH to switch on LED
                print("LED ON!")
            except KeyboardInterrupt:  # Turn LED off before stopping
                digitalWrite(self.led, 0)
                print()
            except IOError:  # Print "Error" if communication error encountered
                print("Error")
        elif type == 1:
            try:
                # Blink the LED
                if self.timer.isDone():
                    self.timer.start()
                    if self.blinkState:
                        digitalWrite(self.led, 1)  # Send HIGH to switch on LED
                        # print("LED ON!")
                    if not self.blinkState:
                        digitalWrite(self.led, 0)  # Send LOW to switch off LED
                        # print("LED OFF!")
                    self.blinkState = not self.blinkState

            except KeyboardInterrupt:  # Turn LED off before stopping
                digitalWrite(self.led, 0)

            except IOError:  # Print "Error" if communication error encountered
                print("Error")

    def off(self):
        try:
            digitalWrite(self.led, 0)  # Send LOW to switch off LED
            print("LED OFF!")
        except IOError:  # Print "Error" if communication error encountered
            print("Error")


class Timer():
    def __init__(self, time):
        self.time = time
        self.timeUntil = datetime.datetime.now()
        self.started = False
    
    def start(self):
        self.timeUntil = datetime.datetime.now() + datetime.timedelta(seconds=self.time)
        self.started = True
    
    def isDone(self):
        done = datetime.datetime.now() >= self.timeUntil
        return done
    
    def stop(self):
        self.timeUntil = datetime.datetime.now()
        self.started = False


if __name__ == "__main__":
    print("Startet")
    led1 = LED(1)
    while True:
        led1.on(1)
        time.sleep(0.05)


