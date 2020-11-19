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
