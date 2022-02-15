from chore import Chore

class Day:
    index: int = None
    name: str = None 
    chores: list[Chore] = None

    def __init__(self, index: int, name: str):
        self.index = index
        self.name = name
        # self.chores = NULL

    def setChores(self, chores) -> None:
        if(self.chores != None):
            for chore in chores:
                self.chores.append(chore)
        else:
            self.chores = chores

    def getChoreString(self) -> str:
        returnString = "**" + self.name + "**" + "\n\n"
        for chore in self.chores:
            returnString += chore.getChoreString() + "\n\n"

        return returnString