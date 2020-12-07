import grovepi
import time
import math

class BuzzerCountdown:
    def __init__(self, pin, totalTimeOn, interval):
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")
        self.totalOnTime = totalTimeOn*60+time.time()
        self.lastBuzz = time.time()
        self.interval = interval
        self.isOn = False
    
    def on(self):
        if time.time() >= self.lastBuzz + self.interval and not self.isOn:
            grovepi.digitalWrite(self.pin, 1)
            self.isOn = True
        if time.time() >= self.lastBuzz + self.interval + 0.15 and self.isOn:
            grovepi.digitalWrite(self.pin, 0)
            self.lastBuzz = time.time()
            self.isOn = False
            # opdater tid interval
            buzzTimer = self.totalOnTime - time.time()
            if buzzTimer <= 3.32:
                buzzTimer = 3.32
            self.interval = math.log10(buzzTimer+5)*5 - 4.5
            print("Timer: {} og Buzz: {}".format(self.totalOnTime - time.time(), self.interval))


    def off(self):
        grovepi.digitalWrite(self.pin, 0)

        

        
        



