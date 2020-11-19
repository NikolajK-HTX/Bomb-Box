# import grovepi


class button():
    def __init__(self, pin):
        self.button = pin
        # grovepi.pinMode(button, "INPUT")

    def buttonCheck(self):
        try:
            # self.buttonState = grovepi.digitalRead(button)
            print()
        except IOError:
            print("Error")
