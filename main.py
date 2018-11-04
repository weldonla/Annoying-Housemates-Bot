
import os
import sys
import numpy as np
from threading import Thread
# from the orginal Telegram API
from telegram import InlineKeyboardButton, KeyboardButton
from telegram import InlineKeyboardMarkup, ReplyKeyboardMarkup
# The Updater class continuously fetches new updates from telegram and passes them on to the Dispatcher class
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import ConversationHandler
from telegram.ext import RegexHandler
from telegram.ext import MessageHandler, Filters
# we set up the logging module, so you will know when (and why) things don't work as expected (see Exception Handling in docs)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

listOfNames = []
keyboardPerson = []
updater = Updater(token='689983690:AAGWebQs6h-7vRAIKK6mMDUk-arnxI3htmk')
dispatcher = updater.dispatcher

NAME, DAY, TASK = range(3)

singleSchedule = ""
listOfSchedules = []

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
def add_name(bot, update):
    username = get_username(update.message.from_user)
    name = get_firstname(update.message.from_user)
    if username not in listOfNames:
        listOfNames.append(username)
        update.message.reply_text("Hey " + name + ", you're now in the schedule. Make sure you do your chores and not be a butthole!")
    else:
        update.message.reply_text("Hey " + name + ", I like your enthusiasm, but you're already in the schedule. You good boy")
    
    bot.send_message(chat_id=update.message.chat_id, text="Here's the current list of added housemates: (here's to go to /schedule)")
    bot.send_message(chat_id=update.message.chat_id, text=listOfNames)

# start() is a function that should process a specific type of update
# sendMessage() - use this method to send messages
def startMessage(bot, update):
    name = get_firstname(update.message.from_user)
    bot.send_message(chat_id=update.message.chat_id, text="Hi " + name + ", welcome to Annoying Housemates Bot!")
    bot.send_message(chat_id=update.message.chat_id, text="As your legit mom, I'm here to help you make sure you and your housemates clean after yourselves, help you schedule your house's duty roster, and try live decent lives.")
    bot.send_message(chat_id=update.message.chat_id, text="Start by pressing the /help command.")

# /help command
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Here's a couple of commands that you should use:\n\n- /help - shows the list of commands\n\n- /addme - include yourself to the schedule. IMPORTANT: if you haven't yet, do this first before you run the /schedule command for the first time!\n\n- /schedule - organize your cleaning rosters. Pick who gets to do what, and when in a week. IMPORTANT: make sure you have run /addme at least once before running /schedule for the first time!\n\n- /showschedule - shows all scheduled tasks\n\n/deleteschedule - remove a schedule\n\n- /start - diplay welcome screen and message\n\nADMIN ONLY:\n- /stop - kill the bot\n- /restart - reboot the bot when it becomes laggy")

#####################################################################################
# /schedule
def schedule(bot, update):
    keyboardPerson = [(np.asarray(listOfNames))]
    
    reply_markup_person = ReplyKeyboardMarkup(keyboardPerson, one_time_keyboard=True)
    
    bot.send_message(chat_id=update.message.chat_id, text='Select person:', reply_markup=reply_markup_person)
    #update.message.reply_text(chat_id=update.message.chat_id, text="", 
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    
    
    count = 100000000
    while count > 0:
        # do nothing
        count = count - 1

    keyboardDay = [[InlineKeyboardButton("Monday"), InlineKeyboardButton("Tuesday"), InlineKeyboardButton("Wednesday")], 
                    [InlineKeyboardButton("Thursday"), InlineKeyboardButton("Friday"), InlineKeyboardButton("Saturday")], 
                    [InlineKeyboardButton("Sunday")]]
    
    reply_markup_day = ReplyKeyboardMarkup(keyboardDay, one_time_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id, text='Select day:', reply_markup=reply_markup_day)

    count = 100000000
    while count > 0:
        # do nothing
        count = count - 1

    keyboardTask = [[InlineKeyboardButton("throw away trash"), InlineKeyboardButton("buy groceries")], [InlineKeyboardButton("do the dishes")]]
    reply_markup_task = ReplyKeyboardMarkup(keyboardTask, one_time_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id, text='Select task:', reply_markup=reply_markup_task)
    
# /showschedule
def showschedule(bot, update):
    for sched in listOfSchedules:
        bot.send_message(chat_id=update.message.chat_id, text=sched)

#/remove-schedule

# /cancel
def cancel(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Cancelling...done")
    return
#end schedule
#####################################################################################


# yell on command (ha!) and via inline mode
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(bot, update):
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
    bot.answer_inline_query(update.inline_query.id, results)

# command to stop the bot using /stop
def stopBot(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Don't be annoying, be a good roommate. Stopping the bot now. Bye!")
    #sys.exit("exited!")
    updater.stop()

# checks for name input and processes it
def name_response(bot, update):
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

def day_response(bot, update):
    query = update.message.text
    selected_day = query
    reply = "Selected day is " + selected_day

    singleSchedule = query + " : "
    update.message.reply_text(reply)
    return ConversationHandler.END

def task_response(bot, update):
    query = update.message.text
    selected_task = query
    reply = "Selected task is " + selected_task
    singleSchedule = query
    listOfSchedules.append(singleSchedule)
    update.message.reply_text(reply)
    return ConversationHandler.END

# a command filter to reply to all commands that were not recognized by the previous handlers.
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command. Press /help for list of commands.")

'''
# function that echoes all messages
def echoMessages(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

# function that turns messages into caps
def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)
'''
'''
def processInput(bot, update):
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
    add_name_handler = CommandHandler('addme', add_name)
    dispatcher.add_handler(add_name_handler)
    
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
    stop_handler = CommandHandler('stop', stopBot, filters=Filters.user(username='@mujahidFA'))
    dispatcher.add_handler(stop_handler)


    # Add /showschedule handler
    showschedule_handler = CommandHandler('showschedule', showschedule)
    dispatcher.add_handler(showschedule_handler)


    schedule_handler = ConversationHandler(
        entry_points=[CommandHandler('schedule', schedule)],
        states={
            NAME: [RegexHandler('^(mujahidFA|mirzanor)$', name_response)],
            DAY: [RegexHandler('^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)$', day_response)],
            TASK: [RegexHandler('^(throw away trash|buy groceries|do the dishes)$', task_response)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(schedule_handler)

    #####################################################################################
    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(bot, update):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()
        update.message.reply_text("You're good to go!")

    dispatcher.add_handler(CommandHandler('restart', restart, filters=Filters.user(username='@mujahidFA')))
    #####################################################################################

   # IMPORTANT: must be added last!!!! unknown command
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    '''
    done = False
    while done == False:
        bot.send_message(chat_id=update.message.chat_id, text="Stopping the bot. Bye!")
    '''
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()