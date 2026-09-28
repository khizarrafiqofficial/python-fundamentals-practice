from random import randint

class train:
    def __init__(slf, trainno):
        slf.trainno = trainno

    def booking(khizar, fro, to):
        print(f"Ticket for train no {khizar.trainno} is booked from {fro} to {to}.")

    def getStatus(slf):
        print(f"The train no {slf.trainno} is running on time.")

    def getFare(slf, fro, to):
        print(f"Ticket fare of train no {slf.trainno} from {fro} to {to} is {randint(222, 6000)}.")


t = train(12954)
t.booking("Karachi", "Lahore")
t.getStatus()
t.getFare("Karachi", "Lahore")
