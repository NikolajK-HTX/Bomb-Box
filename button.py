import grovepi


class button():
    def __init__(self, pin):
        self.button = pin
        grovepi.pinMode(self.button, "INPUT")

    def buttonCheck(self):
        try:
            self.buttonState = grovepi.digitalRead(self.button)
            # print()
        except IOError:
            print("Error")
        return self.buttonState
