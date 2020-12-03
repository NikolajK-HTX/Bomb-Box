import grovepi
import time

class BuzzerCountdown:
    def __init__(self, pin, TotalMinutes, interval):
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")
        self.Total = TotalMinutes
        self.timeTotalStart = time.time()
        self.lastBuzz = 0
        self.interval = interval
    
    def on(self):
        if time.time() >= self.lastBuzz + self.interval:
            grovepi.digitalWrite(self.pin, 1)
        if time.time() >= self.lastBuzz + self.interval + 0.2:
            grovepi.digitalWrite(self.pin, 0)
            self.lastBuzz = time.time()
        
    def changeInterval(self, interval):
        self.interval = interval


        

        
        



