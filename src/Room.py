""" Room class represents classrooms """
class Room:
    def __init__(self, inputString):
        stringParts = inputString.split(",")
        cursorPosition = 0

        self.id = stringParts[cursorPosition].strip()
        cursorPosition += 1

        self.name = stringParts[cursorPosition].strip()
        cursorPosition += 1

        self.capacity = stringParts[cursorPosition].strip()
        cursorPosition += 1

    def printObject(self):
        print "Room: " + str(self.id)
        print "Name: " + str(self.name)
        print "Capacity: " + str(self.capacity)
