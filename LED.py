import time
#from grovepi import *
import random

# Connect the Grove LED to digital port D4
led = 4

light = True



print(
    "This example will blink a Grove LED connected to the GrovePi+ on the port labeled D4. If you're having trouble seeing the LED blink, be sure to check the LED connection and the port number. You may also try reversing the direction of the LED on the sensor.")
print(" ")
print("Connect the LED to the port labele D4!")


def LED():
    # pinMode(led, "OUTPUT")
    time.sleep(1)

    color = random.randint(0, 2)
    if color == 0:
        solid("RED")

    elif color == 1:
        solid("GREEN")
    elif color == 2:
        solid("BLUE")

def blink(color):
    while light:
        try:
            # Blink the LED
            # digitalWrite(led, 1)  # Send HIGH to switch on LED
            print("{} LED ON!".format(color))
            time.sleep(0.5)

            # digitalWrite(led, 0)  # Send LOW to switch off LED
            print("{} LED OFF!".format(color))
            time.sleep(0.5)

        except KeyboardInterrupt:  # Turn LED off before stopping
            # digitalWrite(led, 0)
            break
        except IOError:  # Print "Error" if communication error encountered
            print("Error")


def solid(color):
    try:
        # digitalWrite(led, 1)  # Send HIGH to switch on LED
        print("{} LED ON!".format(color))
    except KeyboardInterrupt:  # Turn LED off before stopping
        # digitalWrite(led, 0)
        print()
    except IOError:  # Print "Error" if communication error encountered
        print("Error")


def off(color):
    try:
        # digitalWrite(led, 0)  # Send HIGH to switch on LED
        print("{} LED OFF!".format(color))
    except KeyboardInterrupt:  # Turn LED off before stopping
        # digitalWrite(led, 0)
        print()
    except IOError:  # Print "Error" if communication error encountered
        print("Error")

LED()

