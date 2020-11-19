import time
#from grovepi import *
import random


class LED():
    def __init__(self, pin):
        self.led = pin
        # pinMode(self.led, "OUTPUT")

    def on(self, type):
        if type == 0:
            try:
                # digitalWrite(self.led, 1)  # Send HIGH to switch on LED
                print("LED ON!")
            except KeyboardInterrupt:  # Turn LED off before stopping
                # digitalWrite(self.led, 0)
                print()
            except IOError:  # Print "Error" if communication error encountered
                print("Error")
        elif type == 1:
            try:
                # Blink the LED
                # digitalWrite(self.led, 1)  # Send HIGH to switch on LED
                print("LED ON!")
                time.sleep(0.5)

                # digitalWrite(self.led, 0)  # Send LOW to switch off LED
                print("LED OFF!")
                time.sleep(0.5)

            except KeyboardInterrupt:  # Turn LED off before stopping
                # digitalWrite(self.led, 0)
                print()
            except IOError:  # Print "Error" if communication error encountered
                print("Error")
