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
                        # Morning
                        Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.EMPTY_COMPOST, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 2, [UserNamesEnum.Luke], ChoreListEnum.FEED_CROWS, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 3, [UserNamesEnum.Luke], ChoreListEnum.WATER_CATS, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 4, [UserNamesEnum.Luke], ChoreListEnum.CHECK_FOR_EGGS, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 5, [UserNamesEnum.Luke], ChoreListEnum.FEED_BEAR_BREAKFAST, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        Chore(idBase + 6, [UserNamesEnum.Luke], ChoreListEnum.WATER_BEAR, datetime(2022, 2, 7, 7, 30).time(), 60, True),
                        # Afternoon
                        Chore(idBase + 7, [UserNamesEnum.Luke], ChoreListEnum.FEED_BEAR_LUNCH, datetime(2022, 2, 7, 12, 30).time(), 60, True),
                        # Evening
                        Chore(idBase + 8, [UserNamesEnum.Luke], ChoreListEnum.CHECK_MAIL, datetime(2022, 2, 7, (4 + 12), 30).time(), 60, True),
                        Chore(idBase + 9, [UserNamesEnum.Luke], ChoreListEnum.FEED_CATS, datetime(2022, 2, 7, (6 + 12), 30).time(), 60, True),
                        Chore(idBase + 10, [UserNamesEnum.Luke], ChoreListEnum.FEED_BEAR_DINNER, datetime(2022, 2, 7, (6 + 12), 30).time(), 60, True),
                        Chore(idBase + 11, [UserNamesEnum.Luke], ChoreListEnum.WATER_BEAR, datetime(2022, 2, 7, (6 + 12), 30).time(), 60, True),
                        Chore(idBase + 12, [UserNamesEnum.Luke], ChoreListEnum.FEED_CHICKENS, datetime(2022, 2, 7, (6 + 12), 30).time(), 60, True),
                        Chore(idBase + 13, [UserNamesEnum.Luke], ChoreListEnum.FEED_COWS, datetime(2022, 2, 7, (6 + 12), 30).time(), 60, True),

                        # Nat
                        Chore(idBase + 14, [UserNamesEnum.Nat], ChoreListEnum.CLEAN_DISHES, datetime(2022, 2, 7, (10 + 12), 30).time(), 60, True),
                        Chore(idBase + 15, [UserNamesEnum.Nat], ChoreListEnum.KITCHEN_COUNTERS, datetime(2022, 2, 7, (10 + 12), 30).time(), 60, True),

                        # James
                        Chore(idBase + 16, [UserNamesEnum.James], ChoreListEnum.EMPTY_DISHWASHER, datetime(2022, 2, 7, (5 + 12), 30).time(), 60, True),
                        Chore(idBase + 17, [UserNamesEnum.James], ChoreListEnum.FILL_DISHWASHER, datetime(2022, 2, 7, (10 + 12), 30).time(), 60, True),
                    ]
                )

                idBase += 17

        # 1st Monday
        self.weeks[0].days[0].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat, UserNamesEnum.Luke, UserNamesEnum.Jake], ChoreListEnum.HAVE_CHAPTER_MEETING, datetime(2022, 2, 7, (6 + 12), 0).time(), 60*24, False),

                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (5 + 12), 0).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.TAKE_OUT_PUT_AWAY_PUB_DISHES, datetime(2022, 2, 7, (5 + 12), 30).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.BRING_IN_PUB_DISHES, datetime(2022, 2, 7, (10 + 12), 30).time(), 1*60, False),
            ]
        )
        idBase += 1
        # 1st Tuesday
        self.weeks[0].days[1].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.COOK_DINNER, datetime(2022, 2, 7, (5 + 12), 30).time(), 4*60, False), 
            ]
        )
        idBase += 7
        # 1st Wednesday
        self.weeks[0].days[2].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.POKE_PEOPLE, datetime(2022, 2, 7, (12), 30).time(), 1*60, False),
            ]
        )
        idBase += 3
        # 1st Thursday
        self.weeks[0].days[3].setChores(
            [
                # Thursday chores day (bi weekly tasks)
                # James
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.KITCHEN_STOVE, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.MOP_KITCHEN, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.SWEEP_HALLS_AND_HALF_BATH, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.SWEEP_STAIRS, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.SWEEP_FULL_BATH, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.CLEAN_PUB_COUCH, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),

                # Nat
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.DO_HOUSE_LAUNDRY, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.BEAT_FLOOR_MATS, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_LIVING_R, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.SWEEP_DINING_R, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.WIPE_DINING_ROOM_TABLES, datetime(2022, 2, 7, (5 + 12), 0).time(), 2*60, False),

                # Not sure if i want to put these here (weekly tasks)
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.SWEEP_KITCHEN, datetime(2022, 2, 7, (5 + 12), 30).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.BURN_TRASH, datetime(2022, 2, 7, (5 + 12), 30).time(), 2*60, False),
                
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.WIPE_LIVING_ROOM_TABLES, datetime(2022, 2, 7, (5 + 12), 30).time(), 2*60, False),
            ]
        )
        idBase += 12
        # 1st Friday
        self.weeks[0].days[4].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (5 + 12), 0).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.TAKE_OUT_PUT_AWAY_PUB_DISHES, datetime(2022, 2, 7, (5 + 12), 30).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.BRING_IN_PUB_DISHES, datetime(2022, 2, 7, (10 + 12), 30).time(), 1*60, False),
            ]
        )
        idBase += 1
        # 1st Saturday
        self.weeks[0].days[5].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Jake], ChoreListEnum.CHECK_ELECTRIC_FENCE, datetime(2022, 2, 7, 7, 30).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CHECK_RECYCLING, datetime(2022, 2, 7, 7, 30).time(), 1*60, False),

                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.GO_SHOPPING, datetime(2022, 2, 7, 10, 30).time(), 2*60, False), 
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.FOOD_PREP, datetime(2022, 2, 7, (12), 30).time(), 4*60, False), 
            ]
        )
        idBase += 1
        # 1st Sunday
        self.weeks[0].days[6].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.PICK_UP_WATER, datetime(2022, 2, 7, 11, 0).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.FOOD_PREP, datetime(2022, 2, 7, (12), 30).time(), 4*60, False), 
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.COOK_DINNER, datetime(2022, 2, 7, (5 + 12), 30).time(), 4*60, False), 
            ]
        )
        idBase += 1

        # 2nd Monday
        self.weeks[1].days[0].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (5 + 12), 0).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.TAKE_OUT_PUT_AWAY_PUB_DISHES, datetime(2022, 2, 7, (5 + 12), 30).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.BRING_IN_PUB_DISHES, datetime(2022, 2, 7, (10 + 12), 30).time(), 1*60, False),
            ]
        )
        idBase += 1
        # 2nd Tuesday
        self.weeks[1].days[1].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CREATE_TASK_LIST, datetime(2022, 2, 7, (12), 30).time(), 24*60, False),
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.COOK_DINNER, datetime(2022, 2, 7, (5 + 12), 30).time(), 4*60, False), 
            ]
        )
        idBase += 6
        # 2nd Wednesday
        self.weeks[1].days[2].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.POKE_PEOPLE, datetime(2022, 2, 7, (12), 30).time(), 1*60, False),
            ]
        )
        idBase += 3
        # 2nd Thursday
        self.weeks[1].days[3].setChores(
            [
                # Not sure if i want to put these here (weekly tasks)
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.SWEEP_KITCHEN, datetime(2022, 2, 7, (5 + 12), 30).time(), 2*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.BURN_TRASH, datetime(2022, 2, 7, (5 + 12), 30).time(), 2*60, False),
                
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.WIPE_LIVING_ROOM_TABLES, datetime(2022, 2, 7, (5 + 12), 30).time(), 2*60, False),
            ]
        )
        idBase += 12
        # 2nd Friday
        self.weeks[1].days[4].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CLEAN_BAR, datetime(2022, 2, 7, (5 + 12), 0).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.TAKE_OUT_PUT_AWAY_PUB_DISHES, datetime(2022, 2, 7, (5 + 12), 30).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.James], ChoreListEnum.BRING_IN_PUB_DISHES, datetime(2022, 2, 7, (10 + 12), 30).time(), 1*60, False),
            ]
        )
        idBase += 1
        # 2nd Saturday
        self.weeks[1].days[5].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.Jake], ChoreListEnum.CHECK_ELECTRIC_FENCE, datetime(2022, 2, 7, 7, 30).time(), 1*60, False),
                Chore(idBase + 1, [UserNamesEnum.Luke], ChoreListEnum.CHECK_RECYCLING, datetime(2022, 2, 7, 7, 30).time(), 1*60, False),
                
                Chore(idBase + 1, [UserNamesEnum.Nat], ChoreListEnum.GO_SHOPPING, datetime(2022, 2, 7, 10, 30).time(), 2*60, False), 
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.FOOD_PREP, datetime(2022, 2, 7, (12), 30).time(), 4*60, False), 
            ]
        )
        idBase += 1
        # 2nd Sunday
        self.weeks[1].days[6].setChores(
            [
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.FOOD_PREP, datetime(2022, 2, 7, (12), 30).time(), 4*60, False), 
                Chore(idBase + 1, [UserNamesEnum.James, UserNamesEnum.Nat], ChoreListEnum.COOK_DINNER, datetime(2022, 2, 7, (5 + 12), 30).time(), 4*60, False), 
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