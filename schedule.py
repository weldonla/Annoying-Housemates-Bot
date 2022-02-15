from chore import Chore
from choreListEnum import ChoreListEnum
from datetime import date, datetime
from choreStatusEnum import ChoreStatusEnum
from day import Day
from userNamesEnum import UserNamesEnum
from week import Week


class Schedule:
    weeks: list[Week] = None
    
    def __init__(self, weeks: list[Week] = None):
        self.weeks = weeks

    def loadWeeksWithChoreDays(self) -> None:
        self.weeks = [
            Week(0, [Day(0, "Monday"), Day(1, "Tuesday"), Day(2, "Wednesday"), Day(3, "Thursday"), Day(4, "Friday"), Day(5, "Saturday"), Day(6, "Sunday")]),
            Week(1, [Day(0, "Monday"), Day(1, "Tuesday"), Day(2, "Wednesday"), Day(3, "Thursday"), Day(4, "Friday"), Day(5, "Saturday"), Day(6, "Sunday")])
        ]
        # Daily Chores
        idBase = 0
        for week in self.weeks:
            for day in week.days:
                day.setChores(
                    [
                        Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.EMPTY_DISHWASHER, datetime(2022, 2, 7, 11, 0).time(), 60),
                        Chore(idBase + 2, [UserNamesEnum.Luke], ChoreListEnum.FEED_AND_WATER_ANIMALS, datetime(2022, 2, 7, 7, 0).time(), 60),
                        Chore(idBase + 3, [UserNamesEnum.Luke], ChoreListEnum.CHECK_ELECTRIC_FENCE, datetime(2022, 2, 7, 7, 0).time(), 60),
                        Chore(idBase + 4, [UserNamesEnum.Luke], ChoreListEnum.CHECK_FOR_EGGS, datetime(2022, 2, 7, 7, 0).time(), 60),
                        Chore(idBase + 5, [UserNamesEnum.Luke], ChoreListEnum.FEED_COWS, datetime(2022, 2, 7, 12, 0).time(), 60),
                        Chore(idBase + 6, [UserNamesEnum.Nat], ChoreListEnum.CHECK_MAIL, datetime(2022, 2, 7, 16, 0).time(), 60),
                        Chore(idBase + 7, [UserNamesEnum.Luke], ChoreListEnum.FEED_AND_WATER_ANIMALS, datetime(2022, 2, 7, 17, 30).time(), 60),
                        Chore(idBase + 8, [UserNamesEnum.James], ChoreListEnum.BRING_IN_PUB_DISHES, datetime(2022, 2, 7, 19, 0).time(), 60),
                        Chore(idBase + 9, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.CLEAN_DISHES, datetime(2022, 2, 7, 22, 0).time(), 60),
                    ]
                )

                idBase += 9

        # 1st Monday
        self.weeks[0].days[0].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.LAUNDRY, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.KITCHEN_COUNTERS, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 3, [UserNamesEnum.Nat], ChoreListEnum.KITCHEN_STOVE, datetime(2022, 2, 7, 11, 0).time(), 180),
                Chore(idBase + 4, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, 17, 0).time(), 120)
            ]
        )
        idBase += 4
        # 1st Tuesday
        self.weeks[0].days[1].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.BEAT_FLOOR_MATS, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_KITCHEN, datetime(2022, 2, 7, 11, 0).time(), 180)
            ]
        )
        idBase += 2
        # 1st Wednesday
        self.weeks[0].days[2].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_LIVING_R, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_DINING_R, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 3, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_HALLS, datetime(2022, 2, 7, 11, 0).time(), 180)
            ]
        )
        idBase += 3
        # 1st Thursday
        self.weeks[0].days[3].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.CLEAN_FULL_BATH, datetime(2022, 2, 7, 11, 0).time(), 180),
                Chore(idBase + 2, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.BURN_TRASH_EMPTY_COMPOST, datetime(2022, 2, 7, 12, 0).time(), 180)
            ]
        )
        idBase += 2
        # 1st Friday
        self.weeks[0].days[4].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.DINING_R_TABLES, datetime(2022, 2, 7, 11, 0).time(), 60), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.LIVING_R_TABLES, datetime(2022, 2, 7, 11, 0).time(), 60),
                Chore(idBase + 3, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, 17, 0).time(), 120)
            ]
        )
        idBase += 3
        # 1st Saturday
        self.weeks[0].days[5].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.SHOPPING, datetime(2022, 2, 7, 10, 0).time(), 180),
                Chore(idBase + 2, [UserNamesEnum.James], ChoreListEnum.REMIND_PEOPLE, datetime(2022, 2, 7, 10, 0).time(), 180)
            ]
        )
        idBase += 2
        # 1st Sunday
        self.weeks[0].days[6].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.ENTER_INCOME, datetime(2022, 2, 7, 12, 0).time(), 180)
            ]
        )
        idBase += 1

        # 2nd Monday
        self.weeks[1].days[0].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.LAUNDRY, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.KITCHEN_COUNTERS, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 3, [UserNamesEnum.Nat], ChoreListEnum.KITCHEN_STOVE, datetime(2022, 2, 7, 11, 0).time(), 180),
                Chore(idBase + 4, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, 17, 0).time(), 120)
            ]
        )
        idBase += 4
        # 2nd Tuesday
        self.weeks[1].days[1].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_KITCHEN, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.MOP_KITCHEN, datetime(2022, 2, 7, 11, 0).time(), 180)
            ]
        )
        idBase += 2
        # 2nd Wednesday
        self.weeks[1].days[2].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_LIVING_R, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_DINING_R, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 3, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_HALLS, datetime(2022, 2, 7, 11, 0).time(), 180)
            ]
        )
        idBase += 3
        # 2nd Thursday
        self.weeks[1].days[3].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.CLEAN_HALF_BATH, datetime(2022, 2, 7, 11, 0).time(), 180),
                Chore(idBase + 2, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.BURN_TRASH_EMPTY_COMPOST, datetime(2022, 2, 7, 12, 0).time(), 180)
            ]
        )
        idBase += 2
        # 2nd Friday
        self.weeks[1].days[4].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.DINING_R_TABLES, datetime(2022, 2, 7, 11, 0).time(), 180), 
                Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.LIVING_R_TABLES, datetime(2022, 2, 7, 11, 0).time(), 180),
                Chore(idBase + 3, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, 17, 0).time(), 120)
            ]
        )
        idBase += 3
        # 2nd Saturday
        self.weeks[1].days[5].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.SHOPPING, datetime(2022, 2, 7, 10, 0).time(), 180),
                Chore(idBase + 2, [UserNamesEnum.James], ChoreListEnum.REMIND_PEOPLE, datetime(2022, 2, 7, 10, 0).time(), 180)
            ]
        )
        idBase += 2
        # 2nd Sunday
        self.weeks[1].days[6].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.CHAPTER, datetime(2022, 2, 7, 15, 0).time(), 120)
            ]
        )
        idBase += 1

    def printWeeksWithChoreDays(self) -> None:
        for week in self.weeks:
            print(week.index)

            for day in week.days:
                print("   " + day.name)

                for chore in day.chores:
                    print("      " + str(chore.id) + ". " + chore.getPeopleString() + " - " + chore.name)

    def getCurrentWeekIndex(self) -> int:
        startDate = date(2022, 1, 24)
        today = date.today()
        weeksDiff = abs(today - startDate).days // 7
        if weeksDiff % 2 == 0:
            return 0
        else:
            return 1

    def getCurrentDayOfChores(self) -> Day:
        currentWeekIndex = self.getCurrentWeekIndex()

        return self.weeks[currentWeekIndex].days[date.today().weekday()]

    def getOutstandingChoresDaysFromPrevious(self) -> list[Day]:
        days: list[Day] = []
        for week in self.weeks:
            for day in week.days:
                for chore in day.chores:
                    if week.index == self.getCurrentWeekIndex() and date.today().weekday() == day.index:
                        break
                    if chore.lastSent != None and chore.status != ChoreStatusEnum.COMPLETE:
                        days.append(day)
                        break
        return days

    def getChoreDaysList(self) -> list[Day]:
        days: list[Day] = []
        days += self.getOutstandingChoresDaysFromPrevious()
        days.append(self.getCurrentDayOfChores())
        return days