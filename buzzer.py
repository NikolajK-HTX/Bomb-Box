import grovepi
import time

class BuzzerCountdown:
    def __init__(self, pin, totalTimeOn, interval):
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")
        self.totalOnTime = totalTimeOn*60+time.time()
        self.lastBuzz = time.time()
        self.interval = interval
        self.isOn = False
    
    def on(self):
        if self.totalOnTime - time.time() <= 30 and self.interval != 2:
            self.interval = 2
        elif self.totalOnTime - time.time() <= 10 and self.interval != 1:
            self.interval = 1
        elif self.totalOnTime - time.time() <= 5 and self.interval != 0.4:
            self.interval = 0.4
        elif self.totalOnTime - time.time() <= 3 and self.interval != 0.25:
            self.interval = 0.25


        if time.time() >= self.lastBuzz + self.interval and not self.isOn:
            grovepi.digitalWrite(self.pin, 1)
            self.isOn = True
        if time.time() >= self.lastBuzz + self.interval + 0.2 and self.isOn:
            grovepi.digitalWrite(self.pin, 0)
            self.lastBuzz = time.time()
            self.isOn = False

    def off(self):
        grovepi.digitalWrite(self.pin, 0)

        

        
        



