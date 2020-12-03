import grovepi
import time

class BuzzerCountdown:
    def __init__(self, pin, TotalMinutes, interval):
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")
        self.Total = TotalMinutes
        self.timeTotalStart = time.time()
        self.lastBuzz = time.time()
        self.interval = interval
        self.on = False
    
    def on(self):
        if time.time() >= self.lastBuzz + self.interval and not self.on:
            grovepi.digitalWrite(self.pin, 1)
            self.on = True
        if time.time() >= self.lastBuzz + self.interval + 0.2 and self.on:
            grovepi.digitalWrite(self.pin, 0)
            self.lastBuzz = time.time()
            self.on = False
        
    def changeInterval(self, interval):
        self.interval = interval


        

        
        



