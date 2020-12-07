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
        if time.time() >= self.lastBuzz + self.interval + 0.2 and self.isOn:
            grovepi.digitalWrite(self.pin, 0)
            self.lastBuzz = time.time()
            self.isOn = False
            # opdater tid interval
            buzzTimer = self.totalOnTime - time.time()
            if buzzTimer <= 1:
                buzzTimer = 1
            self.interval = abs(3*math.log10(buzzTimer))


    def off(self):
        grovepi.digitalWrite(self.pin, 0)

        

        
        



