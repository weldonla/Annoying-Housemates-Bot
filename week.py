from day import Day


class Week:
    index: int = None
    days: list[Day] = None

    def __init__(self, index: int, days: list[Day]):
        self.index = index
        self.days = days

    def setChoreDoneById(self, choreId: int) -> None:
        for day in self.days:
            for chore in day.chores:
                if chore.checkIsComplete() == False:
                    if chore.id == choreId:
                        chore.setStatusComplete()