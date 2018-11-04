# Annoying-Housemates-Bot
A Telegram bot to automate organizing house chores and delegating tasks.

Tired of cleaning your apartment you share with 3 other people by yourself? Sick of being the only one cleaning up the bathroom every week when no one even bats an eye? Ever feel like punching someone in the gut after coming back home to a pile of dishes that was already there sitting nonchalantly in the sink for almost a week?

Introducing: *Annoying Housemates Bot*, a Telegram bot that can let you assign house chores and set a day. Add the Annoying Housemates Bot to your house/apartment chat group on Telegram now, and you'll never be sorry for being passive aggressive to your irresponsible roommates!

Note: this project was made during [VandyHacks 2018](https://vandyhacks.org/). Huge shoutout to them!

# Features
- /help - shows the list of commands

- /addme - include yourself to the schedule. IMPORTANT: if you haven't yet, do this first before you run the /schedule command for the first time!

- /schedule - organize your cleaning rosters. Pick who gets to do what, and when in a week. IMPORTANT: make sure you have run /addme at least once before running /schedule for the first time!

- /showschedule - shows all scheduled tasks

- /start - diplay welcome screen and message

*ADMIN ONLY:*
- /stop - kill the bot

- /restart - reboot the bot when it becomes laggy


# Installation

Annoying Housemates Bot is based of [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and the [Telegram API](https://core.telegram.org/bots/api).

1. Fork the repo.
2. If you don't have them installed, tnstall dependencies:
run '''
pip install -r requirements.txt
'''
This should install python-telegram-bot, and numpy
3. Replace the Bot token with your own. You can get this from @BotFather in Telegram by running on the chat the /token command.
4. run '''
python main.py
'''
