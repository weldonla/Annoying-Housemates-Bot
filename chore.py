from datetime import datetime, timedelta
from choreStatusEnum import ChoreStatusEnum
from userNamesEnum import UserNamesEnum


class Chore:
    id: int = None
    people: list[str] = None
    name: str = None
    startTime: datetime.time = None
    reminderIntervalMinutes: int = None
    status: str = ChoreStatusEnum.INCOMPLETE
    replyToMessageId: int = None
    lastSent: datetime = None
    snoozeDuration: int = None
    isDailyChore: bool = None
    firstSent: datetime = None

    def __init__(self, id: int, people: list[str], name: str, startTime: datetime.time, reminderIntervalMinutes: int, isDailyChore: bool):
        self.id = id
        self.people = people
        self.name = name
        self.startTime = startTime
        self.reminderIntervalMinutes = reminderIntervalMinutes
        self.isDailyChore = isDailyChore
        # self.replyToMessageId = NULL
        # self.lastSent = NULL

    def setFirstSent(self, firstSentDate: datetime):
        self.firstSent = firstSentDate

    def setSnoozeDuration(self, duration: int or None):
        self.snoozeDuration = duration

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
        interval = timedelta(minutes = self.reminderIntervalMinutes)

        if self.status == ChoreStatusEnum.SNOOZE:
            if self.snoozeDuration is not None:
                interval = timedelta(minutes = self.snoozeDuration*60)

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

    def getPeopleShortHandString(self) -> str:
        returnString = ""
        userNamesEnum = UserNamesEnum()
        for x in range(len(self.people)):
            returnString += userNamesEnum.getShortHand(self.people[x])
            if x < len(self.people) - 1:
                returnString += ", "
        
        return returnString
    
    def getPeopleAtString(self) -> str:
        returnString = ""
        for person in self.people:
            returnString += "@" + person + " "
        return returnString
    
    def getEmojiString(self) -> str:
        returnString = ""
        for person in self.people:
            if person == UserNamesEnum.Luke:
                returnString += "⚡️"
            if person == UserNamesEnum.James:
                returnString += "👽"
            if person == UserNamesEnum.Jake:
                returnString += "🍄"
            if person == UserNamesEnum.Nat:
                returnString += "👾"
        return returnString

    def getChoreString(self) -> str:
        time: str = str(self.startTime.hour) + ":" + str(self.startTime.minute)
        return "[" + time + "] <" + self.status[0] + ">: " + self.getPeopleShortHandString() + " " + self.getEmojiString() + " " + " - " + self.name