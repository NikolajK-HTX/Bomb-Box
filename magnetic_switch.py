# encoding=utf-8
import time
import grovepi


class MagneticSwitch:
    def __init__(self, port, name):
        self.port = port
        self.name = name
        grovepi.pinMode(port, "INPUT")
    
    def getValue(self):
        myValue = "Error"
        try:
            myValue = grovepi.digitalRead(self.port)
        except IOError:
            print("Error with reading magnetic switch")
        return myValue


if __name__ == "__main__":
    magnetswitch = MagneticSwitch(6, "rød")
    while True:
        if magnetswitch.getValue() == 1:
            print("En magnet er tæt på, Joe!")
        else:
            print("magneten er længere væk")
        time.sleep(0.2)