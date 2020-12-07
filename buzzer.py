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
            if buzzTimer <= 0.2:
                buzzTimer = 0.2
            self.interval = abs(0*buzzTimer**5 - 0.00001*buzzTimer**4 + 0.00012*buzzTimer**3 + 0.00319*buzzTimer**2 + 0.03283*buzzTimer + 0.02705)
            print("Timer: {} og Buzz: {}".format(buzzTimer, self.interval))


    def off(self):
        grovepi.digitalWrite(self.pin, 0)

        

        
        



