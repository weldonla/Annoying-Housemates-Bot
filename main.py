
from datetime import datetime, timedelta
import os
import sys
import threading
from threading import Thread
import time
from choreStatusEnum import ChoreStatusEnum
# from my classes
from day import Day
from week import Week
from chore import Chore
from choreListEnum import ChoreListEnum
from userNamesEnum import UserNamesEnum
from schedule import Schedule
# from the orginal Telegram API
from telegram import InlineKeyboardButton, KeyboardButton, Message, Update, User
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
from telegram.ext import ConnectionError
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

    keepAwake(update, context)
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
# Routines
#####################################################################################

def keepAwake(update: Update, context: CallbackContext):
    print("Function: keepAwake")
    updater.bot.send_message(chat_id=-795340195, text="Fuck Me Sideways")
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

#####################################################################################
# Helpers
#####################################################################################

async def sendTelegramMessage(update: Update, context: CallbackContext, message: str) -> Message:
    max_tries: int = 10
    for i in range(max_tries):
        try:
            time.sleep(0.3)
            return await updater.bot.send_message(chat_id = update.message.chat_id, text = message)
        except ConnectionError:
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