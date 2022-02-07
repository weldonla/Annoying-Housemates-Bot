from pickle import FALSE, TRUE


class Chore:
    def __init__(self, id, person, name):
        self.id = id
        self.person = person
        self.name = name
        self.status = "INCOMPLETE"

    def setStatusComplete(self):
        self.status = "COMPLETE"

    def checkIsComplete(self):
        if(self.status == "COMPLETE"):
            return TRUE
        else:
            return FALSE