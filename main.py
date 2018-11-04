'''
Commands:
/start - starts the bot
/schedule - lists the whole schedule
/reply-schedule - respond to schedules
/join - add user to the schedule program

##### add user to schedule
/take-out-trash <user> every <time>
/clean-kitchen <user> every <time>
/clean-bathroom <user> every <time>


Admin commands only:
/delete-schedule <user> tasks
/delete-all - delete the whole schedule
/stop - stops the bot from operating
'''
from telegram.ext import Updater
updater = Updater(token='689983690:AAGWebQs6h-7vRAIKK6mMDUk-arnxI3htmk')
dispatcher = updater.dispatcher



# /start command
def start_cmd(bot, update):
    #if count < 2:
        bot.send_message(chat_id=update.message.chat_id, text="Starting the bot!")
    #else:
        #bot.send_message(chat_id=update.message.chat_id, text="Bot already started!")

#def join_cmd():
  
#def schedule_cmd(bot, update):





from telethon import TelegramClient, sync
import telegram

# Use your own values here

api_id = 658475
api_hash = 'f30229c5fb4a761d11b31eed06bfc207'


client = TelegramClient('list_of_group_members', api_id, api_hash)
'''
def collectUser():
    for user in client.iter_participants(Chat.chat_id):
        print(user)
collectUser()
'''
