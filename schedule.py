from chore import Chore
from choreListEnum import ChoreListEnum
from datetime import date, datetime
from choreStatusEnum import ChoreStatusEnum
from day import Day
from userNamesEnum import UserNamesEnum
from week import Week


class Schedule:
    weeks: list[Week] = None
    chatId: any = None
    
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
                        # Luke
                        Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.EMPTY_DISHWASHER, datetime(2022, 2, 7, 10, 30).time(), 120, True),
                        Chore(idBase + 2, [UserNamesEnum.Luke], ChoreListEnum.FEED_AND_WATER_CATS, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 3, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_CAT_LITTER_BOX, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 4, [UserNamesEnum.Luke], ChoreListEnum.BRING_IN_PUB_DISHES, datetime(2022, 2, 7, 7, 30).time(), 120, True),
                        Chore(idBase + 5, [UserNamesEnum.Luke], ChoreListEnum.CHECK_FOR_EGGS, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 6, [UserNamesEnum.Luke], ChoreListEnum.FEED_BEAR_BREAKFAST, datetime(2022, 2, 7, 8, 0).time(), 120, True),
                        Chore(idBase + 7, [UserNamesEnum.Luke], ChoreListEnum.FEED_BEAR_LUNCH, datetime(2022, 2, 7, 12, 30).time(), 120, True),
                        # James
                        Chore(idBase + 8, [UserNamesEnum.James], ChoreListEnum.WATER_BEAR, datetime(2022, 2, 7, 6, 30).time(), 120, True),
                        Chore(idBase + 9, [UserNamesEnum.James], ChoreListEnum.CHECK_MAIL, datetime(2022, 2, 7, (5 + 12), 0).time(), 120, True),
                        Chore(idBase + 10, [UserNamesEnum.James], ChoreListEnum.FEED_BEAR_DINNER, datetime(2022, 2, 7, (6 + 12), 30).time(), 120, True),
                        Chore(idBase + 11, [UserNamesEnum.James], ChoreListEnum.WATER_BEAR, datetime(2022, 2, 7, (6 + 12), 30).time(), 120, True),
                        Chore(idBase + 12, [UserNamesEnum.James], ChoreListEnum.CLEAN_DISHES, datetime(2022, 2, 7, (9 + 12), 0).time(), 120, True),
                        # Nat
                        Chore(idBase + 13, [UserNamesEnum.Nat], ChoreListEnum.WATER_PLANTS, datetime(2022, 2, 7, (4 + 12), 30).time(), 120, True),
                        Chore(idBase + 14, [UserNamesEnum.Nat], ChoreListEnum.WEED_PLANTS, datetime(2022, 2, 7, (4 + 12), 30).time(), 120, True),
                    ]
                )

                idBase += 14

        # 1st Monday
        self.weeks[0].days[0].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (5 + 12), 0).time(), 120, False),
            ]
        )
        idBase += 1
        # 1st Tuesday
        # self.weeks[0].days[1].setChores(
        #     [
        #         Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.KITCHEN_COUNTERS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.DINING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 3, [UserNamesEnum.Nat], ChoreListEnum.LIVING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60),
        #         Chore(idBase + 4, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_DINING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 5, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_LIVING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 6, [UserNamesEnum.Luke], ChoreListEnum.SWEEP_HALLS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60),
        #         Chore(idBase + 7, [UserNamesEnum.Luke], ChoreListEnum.BEAT_FLOOR_MATS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60),
        #     ]
        # )
        # idBase += 7
        # 1st Wednesday
        # self.weeks[0].days[2].setChores(
        #     [
        #     ]
        # )
        # idBase += 3
        # 1st Thursday
        self.weeks[0].days[3].setChores(
            [
            # Luke
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.DINING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 2, [UserNamesEnum.Luke], ChoreListEnum.LIVING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 3, [UserNamesEnum.Luke], ChoreListEnum.BURN_TRASH, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 4, [UserNamesEnum.Luke], ChoreListEnum.CHECK_RECYCLING, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),

            # James
                Chore(idBase + 5, [UserNamesEnum.James], ChoreListEnum.KITCHEN_COUNTERS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 6, [UserNamesEnum.James], ChoreListEnum.CLEAN_KITCHEN_FRIDGE, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 7, [UserNamesEnum.James], ChoreListEnum.EMPTY_COMPOST, datetime(2022, 2, 7, 12, 0).time(), 24*60, False),

            # Nat
                Chore(idBase + 8, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_DINING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 9, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_LIVING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 10, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_HALLS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 11, [UserNamesEnum.Nat], ChoreListEnum.LAUNDRY, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 12, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_KITCHEN, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
            ]
        )
        idBase += 12
        # 1st Friday
        self.weeks[0].days[4].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
            ]
        )
        idBase += 1
        # 1st Saturday
        self.weeks[0].days[5].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.REMIND_PEOPLE, datetime(2022, 2, 7, 10, 0).time(), 24*60, False),
            ]
        )
        idBase += 1
        # 1st Sunday
        self.weeks[0].days[6].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.FOOD_PREP, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
            ]
        )
        idBase += 1

        # 2nd Monday
        self.weeks[1].days[0].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
            ]
        )
        idBase += 1
        # 2nd Tuesday
        # self.weeks[1].days[1].setChores(
        #     [
        #         Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.KITCHEN_COUNTERS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 2, [UserNamesEnum.Nat], ChoreListEnum.DINING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 3, [UserNamesEnum.Nat], ChoreListEnum.LIVING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60),
        #         Chore(idBase + 4, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_DINING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 5, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_LIVING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60), 
        #         Chore(idBase + 6, [UserNamesEnum.Luke], ChoreListEnum.SWEEP_HALLS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60)
        #     ]
        # )
        # idBase += 6
        # 2nd Wednesday
        # self.weeks[1].days[2].setChores(
        #     [
        #     ]
        # )
        # idBase += 3
        # 2nd Thursday
        self.weeks[1].days[3].setChores(
            [
            # Luke
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.DINING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 2, [UserNamesEnum.Luke], ChoreListEnum.LIVING_R_TABLES, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 3, [UserNamesEnum.Luke], ChoreListEnum.BURN_TRASH, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 4, [UserNamesEnum.Luke], ChoreListEnum.CHECK_RECYCLING, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),

            # James
                Chore(idBase + 5, [UserNamesEnum.James], ChoreListEnum.KITCHEN_COUNTERS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 6, [UserNamesEnum.James], ChoreListEnum.CLEAN_KITCHEN_FRIDGE, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 7, [UserNamesEnum.James], ChoreListEnum.EMPTY_COMPOST, datetime(2022, 2, 7, 12, 0).time(), 24*60, False),

            # Nat
                Chore(idBase + 8, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_DINING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 9, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_LIVING_R, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 10, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_HALLS, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 11, [UserNamesEnum.Nat], ChoreListEnum.LAUNDRY, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
                Chore(idBase + 12, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_KITCHEN, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
            ]
        )
        idBase += 12
        # 2nd Friday
        self.weeks[1].days[4].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
            ]
        )
        idBase += 1
        # 2nd Saturday
        self.weeks[1].days[5].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.REMIND_PEOPLE, datetime(2022, 2, 7, 10, 0).time(), 24*60, False),
            ]
        )
        idBase += 1
        # 2nd Sunday
        self.weeks[1].days[6].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.CHAPTER, datetime(2022, 2, 7, (3 + 12), 0).time(), 60*24, False),
                Chore(idBase + 2, [UserNamesEnum.James], ChoreListEnum.FOOD_PREP, datetime(2022, 2, 7, (4 + 12), 30).time(), 24*60, False),
            ]
        )
        idBase += 2

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