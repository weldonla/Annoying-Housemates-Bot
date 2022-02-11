
from datetime import datetime, timedelta
import os
from socket import timeout
import sys
import threading
import numpy as np
from threading import Thread
from choreStatusEnum import ChoreStatusEnum
# from my classes
from day import Day
from week import Week
from chore import Chore
from choreListEnum import ChoreListEnum
from userNamesEnum import UserNamesEnum
from schedule import Schedule
# from the orginal Telegram API
from telegram import InlineKeyboardButton, KeyboardButton, Update
from telegram import InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
# The Updater class continuously fetches new updates from telegram and passes them on to the Dispatcher class
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import ConversationHandler
from telegram.ext import RegexHandler
from telegram.ext import MessageHandler, Filters
# we set up the logging module, so you will know when (and why) things don't work as expected (see Exception Handling in docs)
from telegramToken import Token
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# listOfNames = []
# userNames = [UserNamesEnum.Luke, UserNamesEnum.Jake, UserNamesEnum.Nat, UserNamesEnum.James]
# keyboardPerson = []
updater = Updater(token=Token.token, use_context=True)
dispatcher = updater.dispatcher

# NAME, DAY, TASK = range(3)

# singleSchedule = ""
# listOfSchedules = []

schedule = Schedule()
schedule.loadWeeksWithChoreDays()

# get username of the last chat sender		
def get_username(user):
    try:
        name = user.username
    except (NameError, AttributeError):
        try:
            name = user.first_name
        except (NameError, AttributeError):
            #logger.info("No username or first name.. wtf")
            return	""
    return name

# get first name of the last chat sender		 		
def get_firstname(user):
    try:
        name = user.first_name
    except (NameError, AttributeError):
        try:
            name = user.username
        except (NameError, AttributeError):
            #logger.info("No username or first name.. wtf")
            return	""
    return name

# function that adds name to scheduler list
# def add_name(update, context):
#     username = get_username(update.message.from_user)
#     name = get_firstname(update.message.from_user)
#     if username not in listOfNames:
#         listOfNames.append(username)
#         update.message.reply_text("Hey " + name + ", you're now in the schedule. Make sure you do your chores and not be a butthole!")
#     else:
#         update.message.reply_text("Hey " + name + ", I like your enthusiasm, but you're already in the schedule. You good boy")
    
#     updater.bot.send_message(chat_id=update.message.chat_id, text="Here's the current list of added housemates: (here's to go to /schedule)")
#     updater.bot.send_message(chat_id=update.message.chat_id, text=listOfNames)


#####################################################################################
# Commands
#####################################################################################
# /start command
# start() is a function that should process a specific type of update
# sendMessage() - use this method to send messages
def startMessage(update: Update, context: CallbackContext):
    print("Function: startMessage")
    name = get_firstname(update.message.from_user)
    updater.bot.send_message(chat_id=update.message.chat_id, text="Hi " + name + ", I'm Navi, the Bitch Bot!")
    updater.bot.send_message(chat_id=update.message.chat_id, text="Hey! On your journey you will need someone to remind you and your party of your current objectives.")
    updater.bot.send_message(chat_id=update.message.chat_id, text="Listen! Start by pressing the /help command.")

    # keepAwake(update, context)
    checkChores(update, context)

# /help command
def help(update: Update, context: CallbackContext):
    updater.bot.send_message(chat_id=update.message.chat_id, text="\n\nHey! Listen! Here's a couple of commands that you should use:\n\n- /complete - completes the chore of whatever message you reply to (if that message is the latest reminder for that chore). And brings up a button list if you're not replying to a task.\n\n- /snooze - doubles the bitch interval time for given chore for one bitch iteration.\n\n- /showdayschedule - shows all scheduled tasks for the day\n\n- /start - diplay welcome screen and message\n\nADMIN ONLY:\n- /stop - kill the updater.\n- /restart - reboot the bot when it becomes laggy")

# /complete command
def complete(update: Update, context):
    print("Function: complete")
    chores: list[Chore] = []
    for day in schedule.getChoreDaysList(): 
        chores += day.chores

    if(update.message.reply_to_message is None):
        keyboard = []
        for chore in chores:
            if chore.checkIsComplete() == False:
                keyboard.append([
                    InlineKeyboardButton(
                        "[" + str(chore.id) + "]: " + chore.getPeopleString() + " - " + chore.name + " <" + chore.status + ">", 
                        callback_data=str(chore.id)),
                ])
        reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=True)
        update.message.reply_text("Which chore should be marked as complete?", reply_markup=reply_markup)
        
    else:
        print("   ReplyToMessageId: " + str(update.message.reply_to_message.message_id))
        for chore in chores:
            if chore.replyToMessageId == None:
                continue
            elif chore.replyToMessageId == update.message.reply_to_message.message_id:
                chore.setStatusComplete()
                updater.bot.send_message(chat_id=update.message.chat_id, text=chore.name + " complete")

# Handle reply for /complete command
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    
    print("Function: complete button")

    chores: list[Chore] = []
    for day in schedule.getChoreDaysList(): 
        chores += day.chores

    for chore in chores:
        if(str(chore.id) == query.data):
            chore.setStatusComplete()
            query.answer()
            query.edit_message_text(text=f"Completed Chore: {chore.name}")
            print("   Chore: " + chore.name)

# /showschedule
def showdayschedule(update: Update, context: CallbackContext):
    choresString: str = ""
    for day in schedule.getChoreDaysList(): 
        choresString += day.getChoreString() + "\n"

    updater.bot.send_message(chat_id=update.message.chat_id, text=choresString)

def snooze(update: Update, context: CallbackContext):
    chores: list[Chore] = []
    for day in schedule.getChoreDaysList(): 
        chores += day.chores
    
    for chore in chores:
        if chore.replyToMessageId == None:
            continue
        elif chore.replyToMessageId == update.message.reply_to_message.message_id:
            chore.setStatusSnooze()
            updater.bot.send_message(chat_id=update.message.chat_id, text=chore.name + " snoozing")


#####################################################################################
# /schedule
# def schedule(update, context):
#     keyboardPerson = [listOfNames]
    
#     reply_markup_person = ReplyKeyboardMarkup(keyboardPerson, one_time_keyboard=True)
#     logging.debug(reply_markup_person)
#     updater.bot.send_message(chat_id=update.message.chat_id, text="Select person:", reply_markup=reply_markup_person)
#     logging.debug(reply_markup_person)
#     #update.message.reply_text(chat_id=update.message.chat_id, text="", 
#     updater.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    
    
#     count = 100000000
#     while count > 0:
#         # do nothing
#         count = count - 1

#     keyboardDay = [["Monday"],["Tuesday"],["Wednesday"], 
#                     ["Thursday"],["Friday"],["Saturday"], 
#                     ["Sunday"]]
    
#     reply_markup_day = ReplyKeyboardMarkup(keyboardDay, one_time_keyboard=True)
#     updater.bot.send_message(chat_id=update.message.chat_id, text="Select day:", reply_markup=reply_markup_day)

#     count = 100000000
#     while count > 0:
#         # do nothing
#         count = count - 1

#     keyboardTask = [["throw away trash"], ["buy groceries"], ["do the dishes"]]
#     reply_markup_task = ReplyKeyboardMarkup(keyboardTask, one_time_keyboard=True)
#     updater.bot.send_message(chat_id=update.message.chat_id, text='Select task:', reply_markup=reply_markup_task)
    


#/remove-schedule

# /cancel
# def cancel(update, context):
#     updater.bot.send_message(chat_id=update.message.chat_id, text="Cancelling...done")
#     return
#end schedule
#####################################################################################

#####################################################################################
# Routines
#####################################################################################

def keepAwake(update: Update, context: CallbackContext):
    print("Function: keepAwake")
    updater.bot.send_message(chat_id=-795340195, text="Fuck Me Sideways")
    # updater.stop()
    # updater.start_polling()
    # updater.idle()
    threading.Timer(9.0*60, keepAwake, args=(update, context)).start()

def checkChores(update: Update, context: CallbackContext):
    chores: list[Chore] = []
    for day in schedule.getChoreDaysList(): 
        chores += day.chores

    for chore in chores:
        if chore.status == "COMPLETE":
            continue

        if chore.lastSent == None:
            if datetime(2022, 2, 7, chore.startTime.hour, chore.startTime.minute).time() < datetime.now().time():
                sentMessage = updater.bot.send_message(chat_id=update.message.chat_id, text=chore.getPeopleAtString() + " - " + chore.name, timeout = 60)
                chore.setLastSent()
                chore.setReplyToMessageId(sentMessage.message_id)
        elif chore.isBitchable():
            print(chore.name + ": " + str(chore.lastSent) + "/" + str(chore.reminderIntervalMinutes))
            if chore.status == ChoreStatusEnum.SNOOZE:
                chore.setStatusIncomplete()

            sentMessage = updater.bot.send_message(chat_id=update.message.chat_id, text=chore.getPeopleAtString() + " - " + chore.name, timeout = 60)
            chore.setLastSent()
            chore.setReplyToMessageId(sentMessage.message_id)

    threading.Timer(60.0*5, checkChores, args=(update, context)).start()

# yell on command (ha!) and via inline mode
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    updater.bot.answer_inline_query(update.inline_query.id, results)

# command to stop the bot using /stop
def stopBot(update: Update, context: CallbackContext):
    updater.bot.send_message(chat_id=update.message.chat_id, text="Don't be annoying, be a good roommate. Stopping the bot now. Bye!")
    #sys.exit("exited!")
    updater.stop()

# checks for name input and processes it
def name_response(update: Update, context: CallbackContext):
    query = update.message.text
    reply = ""
    if query == "mujahidFA":
        selected_person = query
        reply = "Selected person is " + selected_person
    else:
        selected_person = query
        reply = "Selected person is " + selected_person

    singleSchedule = query + " : "
    update.message.reply_text(reply)
    return ConversationHandler.END

def day_response(update: Update, context: CallbackContext):
    query = update.message.text
    selected_day = query
    reply = "Selected day is " + selected_day

    singleSchedule = query + " : "
    update.message.reply_text(reply)
    return ConversationHandler.END

def task_response(update: Update, context: CallbackContext):
    query = update.message.text
    selected_task = query
    reply = "Selected task is " + selected_task
    singleSchedule = query
    listOfSchedules.append(singleSchedule)
    update.message.reply_text(reply)
    return ConversationHandler.END

# a command filter to reply to all commands that were not recognized by the previous handlers.
def unknown(update: Update, context: CallbackContext):
    updater.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command. Press /help for list of commands.")

'''
# function that echoes all messages
def echoMessages(update, context):
    updater.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

# function that turns messages into caps
def caps(update, context, args):
    text_caps = ' '.join(args).upper()
    updater.bot.send_message(chat_id=update.message.chat_id, text=text_caps)
'''
'''
def processInput(update, context):
    if update.message.photo:
        compute
'''


def main():
    ################ Add your other handlers here... ##########################
    # /start command
    start_handler = CommandHandler('start', startMessage)
    dispatcher.add_handler(start_handler)

    # /help - help screen
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    
    # /add command - to add name to be considered in schedule
    # add_name_handler = CommandHandler('addme', add_name)
    # dispatcher.add_handler(add_name_handler)

    complete_handler = CommandHandler('complete', complete)
    dispatcher.add_handler(complete_handler)

    complete_button_handler = CallbackQueryHandler(button)
    dispatcher.add_handler(complete_button_handler)
    
    snooze_handler = CommandHandler('snooze', snooze)
    dispatcher.add_handler(snooze_handler)
    
    # /echo command
    #echo_handler = MessageHandler(Filters.text, echoMessages)
    #dispatcher.add_handler(echo_handler)

    # get image
    #dispatcher.add_handler(MessageHandler(Filters.photo, processInput))

    # /caps command
    #caps_handler = CommandHandler('caps', caps, pass_args="true")
    #dispatcher.add_handler(caps_handler)

    # inline utility
    #inline_caps_handler = InlineQueryHandler(inline_caps)
    #dispatcher.add_handler(inline_caps_handler)
    
    # /stop command
    stop_handler = CommandHandler('stop', stopBot, filters=Filters.user(username='@' + UserNamesEnum.Luke))
    dispatcher.add_handler(stop_handler)


    # Add /showschedule handler
    showdayschedule_handler = CommandHandler('showdayschedule', showdayschedule)
    dispatcher.add_handler(showdayschedule_handler)


    # schedule_handler = ConversationHandler(
    #     entry_points=[CommandHandler('schedule', schedule)],
    #     states={
    #         NAME: [RegexHandler('^(mujahidFA|mirzanor)$', name_response)],
    #         DAY: [RegexHandler('^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)$', day_response)],
    #         TASK: [RegexHandler('^(throw away trash|buy groceries|do the dishes)$', task_response)]
    #     },
    #     fallbacks=[CommandHandler('cancel', cancel)]
    # )
    # dispatcher.add_handler(schedule_handler)

    #####################################################################################
    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update, context):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()
        update.message.reply_text("You're good to go!")

    dispatcher.add_handler(CommandHandler('restart', restart, filters=Filters.user(username='@' + UserNamesEnum.Luke)))
    #####################################################################################

   # IMPORTANT: must be added last!!!! unknown command
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    '''
    done = False
    while done == False:
        updater.bot.send_message(chat_id=update.message.chat_id, text="Stopping the bot. Bye!")
    '''
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()