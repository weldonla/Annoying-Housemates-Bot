
from collections import namedtuple
from datetime import datetime, timedelta
import json
import os
import sys
import threading
from threading import Thread
import time
from callbackQuery import CallBackQuery
from choreStatusEnum import ChoreStatusEnum
# from my classes
from day import Day
from typeOfQueryEnum import TypeOfQueryEnum
from week import Week
from chore import Chore
from choreListEnum import ChoreListEnum
from userNamesEnum import UserNamesEnum
from schedule import Schedule
# from the orginal Telegram API
from telegram import InlineKeyboardButton, KeyboardButton, Message, ReplyMarkup, Update, User
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
from telegramToken import Token
# we set up the logging module, so you will know when (and why) things don't work as expected (see Exception Handling in docs)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=Token.token, use_context=True)
dispatcher = updater.dispatcher

schedule = Schedule()
schedule.loadWeeksWithChoreDays()

# get username of the last chat sender		
def get_username(user: User):
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
def get_firstname(user: User):
    try:
        name = user.first_name
    except (NameError, AttributeError):
        try:
            name = user.username
        except (NameError, AttributeError):
            #logger.info("No username or first name.. wtf")
            return	""
    return name

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
    text="\n\nHey! Listen! Here's a couple of commands that you should use:\n\n- /complete - completes the chore of whatever message you reply to (if that message is the latest reminder for that chore). And brings up a button list if you're not replying to a task.\n\n- /snooze - doubles the bitch interval time for given chore for one bitch iteration.\n\n- /showdayschedule - shows all scheduled tasks for the day\n\n- /start - diplay welcome screen and message\n\nADMIN ONLY:\n- /stop - kill the updater.\n- /restart - reboot the bot when it becomes laggy"
    # updater.bot.send_message(chat_id=update.message.chat_id, text="\n\nHey! Listen! Here's a couple of commands that you should use:\n\n- /complete - completes the chore of whatever message you reply to (if that message is the latest reminder for that chore). And brings up a button list if you're not replying to a task.\n\n- /snooze - doubles the bitch interval time for given chore for one bitch iteration.\n\n- /showdayschedule - shows all scheduled tasks for the day\n\n- /start - diplay welcome screen and message\n\nADMIN ONLY:\n- /stop - kill the updater.\n- /restart - reboot the bot when it becomes laggy")
    sendTelegramMessage(update, context, text)

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
                callback: CallBackQuery = CallBackQuery(TypeOfQueryEnum.COMPLETE, chore.id, None)
                jsonCallback: str = json.dumps(callback.__dict__)
                keyboard.append([
                    InlineKeyboardButton(
                        chore.getChoreString(), 
                        callback_data=jsonCallback),
                ])
        reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=True)
        sendTelegramReplyMessage(update, context, "Hey! Which chore should be marked as complete?", reply_markup)
        
    else:
        print("   ReplyToMessageId: " + str(update.message.reply_to_message.message_id))
        for chore in chores:
            if chore.replyToMessageId == None:
                continue
            elif chore.replyToMessageId == update.message.reply_to_message.message_id:
                chore.setStatusComplete()
                sendTelegramMessage(update, context, chore.name + " complete")

# Handle reply for /complete command
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    
    print("Function: complete button")

    chores: list[Chore] = []
    for day in schedule.getChoreDaysList(): 
        chores += day.chores

    callback: CallBackQuery = json.loads(query.data, object_hook=customCallbackDecoder)

    if callback.typeOfQuery == TypeOfQueryEnum.COMPLETE:
        for chore in chores:
            if(chore.id == callback.choreId):
                chore.setStatusComplete()
                query.answer()
                query.edit_message_text(text=f"Completed Chore: {chore.name}")
                print("   Chore: " + chore.getChoreString())

    if callback.typeOfQuery == TypeOfQueryEnum.SNOOZE:
        for chore in chores:
            if(chore.id == callback.choreId):
                chore.setStatusSnooze()
                chore.setSnoozeDuration(callback.data)
                query.answer()
                query.edit_message_text(text=f"Snoozing Chore: {chore.name} for {callback.data} hours")
                print("   Chore: " + chore.getChoreString())

def customCallbackDecoder(callbackDict):
    return namedtuple('X', callbackDict.keys())(*callbackDict.values())

# /showschedule
def showdayschedule(update: Update, context: CallbackContext):
    choresString: str = ""
    for day in schedule.getChoreDaysList(): 
        choresString += day.getChoreString() + "\n"

    # updater.bot.send_message(chat_id=update.message.chat_id, text=choresString)
    sendTelegramMessage(update, context, choresString)

def snooze(update: Update, context: CallbackContext):
    chores: list[Chore] = []
    for day in schedule.getChoreDaysList(): 
        chores += day.chores
    
    for chore in chores:
        if chore.replyToMessageId == None:
            continue
        elif chore.replyToMessageId == update.message.reply_to_message.message_id:
            # chore.setStatusSnooze()
            # updater.bot.send_message(chat_id=update.message.chat_id, text=chore.name + " snoozing")
            # sendTelegramMessage(update, context, chore.name + " snoozing")
            keyboard = [
                [
                    InlineKeyboardButton(
                        "2 Hours", 
                        callback_data=json.dumps(CallBackQuery(TypeOfQueryEnum.SNOOZE, chore.id, 2).__dict__)),
                ],
                [
                    InlineKeyboardButton(
                        "4 Hours", 
                        callback_data=json.dumps(CallBackQuery(TypeOfQueryEnum.SNOOZE, chore.id, 4).__dict__)),
                ],
                [
                    InlineKeyboardButton(
                        "8 Hours", 
                        callback_data=json.dumps(CallBackQuery(TypeOfQueryEnum.SNOOZE, chore.id, 8).__dict__)),
                ],
                [
                    InlineKeyboardButton(
                        "12 Hours", 
                        callback_data=json.dumps(CallBackQuery(TypeOfQueryEnum.SNOOZE, chore.id, 12).__dict__)),
                ],
                [
                    InlineKeyboardButton(
                        "18 Hours", 
                        callback_data=json.dumps(CallBackQuery(TypeOfQueryEnum.SNOOZE, chore.id, 18).__dict__)),
                ],
                [
                    InlineKeyboardButton(
                        "24 Hours", 
                        callback_data=json.dumps(CallBackQuery(TypeOfQueryEnum.SNOOZE, chore.id, 24).__dict__)),
                ],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=True)
            # update.message.reply_text("Which chore should be marked as complete?", reply_markup=reply_markup)
            sendTelegramReplyMessage(update, context, "How Long Do You Wish to Snooze?", reply_markup)

#####################################################################################
# Routines
#####################################################################################

def checkChores(update: Update, context: CallbackContext):
    chores: list[Chore] = []

    # No bitch hours between 2 - 7 am
    if (datetime.now().time() > datetime(2022, 2, 7, 2, 0).time() and datetime.now().time() < datetime(2022, 2, 7, 7, 0).time()) :
        threading.Timer(60.0*5, checkChores, args=(update, context)).start()
        return

    for day in schedule.getChoreDaysList(): 
        chores += day.chores

    for chore in chores:
        if chore.status == ChoreStatusEnum.COMPLETE:
            continue

        if chore.lastSent == None:
            if datetime(2022, 2, 7, chore.startTime.hour, chore.startTime.minute).time() < datetime.now().time():
                # sentMessage = updater.bot.send_message(chat_id=update.message.chat_id, text=chore.getPeopleAtString() + " - " + chore.name, timeout = 60)
                sentMessage = sendTelegramMessage(update, context, chore.getPeopleAtString() + " - " + chore.name)
                chore.setLastSent()
                chore.setReplyToMessageId(sentMessage.message_id)
        elif chore.isBitchable():
            print(str(chore.id) + " - " + chore.name + ": " + str(chore.lastSent) + "/" + str(chore.reminderIntervalMinutes))
            if chore.status == ChoreStatusEnum.SNOOZE:
                chore.setStatusIncomplete()
                chore.setSnoozeDuration(None)

            # sentMessage = updater.bot.send_message(chat_id=update.message.chat_id, text=chore.getPeopleAtString() + " - " + chore.name, timeout = 60)
            sentMessage = sendTelegramMessage(update, context, chore.getPeopleAtString() + " - " + chore.name)
            chore.setLastSent()
            chore.setReplyToMessageId(sentMessage.message_id)

    threading.Timer(60.0*5, checkChores, args=(update, context)).start()

#####################################################################################
# Helpers
#####################################################################################

def sendTelegramMessage(update: Update, context: CallbackContext, message: str) -> Message:
    max_tries: int = 10
    for i in range(max_tries):
        try:
            time.sleep(0.3)
            return updater.bot.send_message(chat_id = update.message.chat_id, text = message, timeout = 60)
        except Exception:
            continue

def sendTelegramReplyMessage(update: Update, context: CallbackContext, text: str, reply_markup: ReplyMarkup) -> Message:
    max_tries: int = 10
    for i in range(max_tries):
        try:
            time.sleep(0.3)
            return update.message.reply_text(text, reply_markup=reply_markup)
        except Exception:
            continue

# command to stop the bot using /stop
def stopBot(update: Update, context: CallbackContext):
    updater.bot.send_message(chat_id=update.message.chat_id, text="Don't be annoying, be a good roommate. Stopping the bot now. Bye!")
    #sys.exit("exited!")
    updater.stop()

# a command filter to reply to all commands that were not recognized by the previous handlers.
def unknown(update: Update, context: CallbackContext):
    updater.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command. Press /help for list of commands.")

def main():
    ################ Add your other handlers here... ##########################
    # /start command
    start_handler = CommandHandler('start', startMessage)
    dispatcher.add_handler(start_handler)

    # /help - help screen
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)

    complete_handler = CommandHandler('complete', complete)
    dispatcher.add_handler(complete_handler)

    complete_button_handler = CallbackQueryHandler(button)
    dispatcher.add_handler(complete_button_handler)
    
    snooze_handler = CommandHandler('snooze', snooze)
    dispatcher.add_handler(snooze_handler)
    
    # /stop command
    stop_handler = CommandHandler('stop', stopBot, filters=Filters.user(username='@' + UserNamesEnum.Luke))
    dispatcher.add_handler(stop_handler)

    # Add /showschedule handler
    showdayschedule_handler = CommandHandler('showdayschedule', showdayschedule)
    dispatcher.add_handler(showdayschedule_handler)

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

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()