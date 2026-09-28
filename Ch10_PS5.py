from random import randint

class train:
    def __init__(self, trainno):
        self.trainno = trainno

    def booking(self, fro, to):
        print(f"Ticket for train no {self.trainno} is booked from {fro} to {to}.")

    def getStatus(self):
        print(f"The train no {self.trainno} is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket fare of train no {self.trainno} from {fro} to {to} is {randint(222, 6000)}.")


t = train(12954)
t.booking("Karachi", "Lahore")
t.getStatus()
t.getFare("Karachi", "Lahore")
