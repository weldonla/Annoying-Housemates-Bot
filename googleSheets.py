from __future__ import print_function
from collections import namedtuple
import json

import pandas as pd
import gspread
from choreDataStructure import ChoreDataStructure
from choreListEnum import ChoreListEnum
from choreStatusEnum import ChoreStatusEnum
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import pprint

from chore import Chore

pp = pprint.PrettyPrinter()

client = gspread.service_account(filename='credentials.json')

def customCallbackDecoder(callbackDict):
    return namedtuple('X', callbackDict.keys())(*callbackDict.values())

def setStatusById(status: ChoreStatusEnum, id: int):
    choresSpreadSheet = client.open('House Chores').get_worksheet_by_id(0)
    df = pd.DataFrame.from_records(get_as_dataframe(choresSpreadSheet)) 

    df.loc[id, "status"] = status
    
    set_with_dataframe(choresSpreadSheet, df)

def resetDailyChores():
    choresSpreadSheet = client.open('House Chores').get_worksheet_by_id(0)
    df = pd.DataFrame.from_records(get_as_dataframe(choresSpreadSheet)) 

    for index in df.index:
        if(df.loc[index, ChoreDataStructure.IS_DAILY_CHORE] == True):
            setStatusById(ChoreStatusEnum.INCOMPLETE, df.loc[index, "id"])
    

def main():
    resetDailyChores()




if __name__ == '__main__':
    main()