from asyncio.windows_events import NULL


class Day:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def setChores(self, chores):
        self.chores = chores