import time
import grovepi
 
# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 6
 
grovepi.pinMode(button,"INPUT")
 
while True:
    try:
        print(grovepi.digitalRead(button))
        time.sleep(.5)
 
    except IOError:
        print ("Error")