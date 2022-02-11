from datetime import datetime, timedelta
from choreStatusEnum import ChoreStatusEnum


class Chore:
    id: int = None
    people: list[str] = None
    name: str = None
    startTime: datetime.time = None
    reminderIntervalMinutes: int = None
    status: str = ChoreStatusEnum.INCOMPLETE
    replyToMessageId: int = None
    lastSent: datetime = None

    def __init__(self, id: int, people: list[str], name: str, startTime: datetime.time, reminderIntervalMinutes: int):
        self.id = id
        self.people = people
        self.name = name
        self.startTime = startTime
        self.reminderIntervalMinutes = reminderIntervalMinutes
        # self.replyToMessageId = NULL
        # self.lastSent = NULL

    def setReplyToMessageId(self, messageId) -> None:
        self.replyToMessageId = messageId

    def setLastSent(self) -> None:
        self.lastSent = datetime.now()

    def setStatusComplete(self) -> None:
        self.status = ChoreStatusEnum.COMPLETE

    def setStatusSnooze(self) -> None:
        self.status = ChoreStatusEnum.SNOOZE
        
    def setStatusIncomplete(self) -> None:
        self.status = ChoreStatusEnum.INCOMPLETE

    def checkIsComplete(self) -> bool:
        if(self.status == ChoreStatusEnum.COMPLETE):
            return True
        else:
            return False

    def setReplyToMessageId(self, messageId) -> None:
        self.replyToMessageId = messageId

    def isBitchable(self) -> bool:
        snoozeMultiplier = 1
        if self.status == ChoreStatusEnum.SNOOZE:
            snoozeMultiplier = 2

        interval = timedelta(minutes = self.reminderIntervalMinutes*snoozeMultiplier)

        if self.lastSent + interval < datetime.now():
            return True
        else:
            return False

    def getPeopleString(self) -> str:
        returnString = ""
        for x in range(len(self.people)):
            returnString += self.people[x]
            if x < len(self.people) - 1:
                returnString += ", "
        
        return returnString
    
    def getPeopleAtString(self) -> str:
        returnString = ""
        for person in self.people:
            returnString += "@" + person + " "
        return returnString