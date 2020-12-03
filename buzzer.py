import grovepi
import time

class BuzzerCountdown:
    def __init__(self, pin, TotalMinutes):
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")
        self.Total = TotalMinutes
        self.buzz = False
        self.count = 0
    
    def on(self):
        if (time.time() >= (time.time() + self.count * 5)) and not self.buzz:
            self.buzz = True
            grovepi.digitalWrite(self.pin, 1)
        elif (time.time() - (time.time() + self.count * 5) >= 0.2) and self.buzz:
            self.buzz = False
            self.count += 1
            grovepi.digitalWrite(self.pin, 0)

        

        
        



