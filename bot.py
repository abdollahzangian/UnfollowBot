from instabot import Bot
from time import sleep
from random import randint
import config

bot = Bot()

bot.login(username=config.username, password=config.password, ask_for_code=True)

non_follow = set(bot.following) - set(bot.followers)

for user in non_follow:
    try:
        bot.unfollow(user)
        sleep(randint(6,20))
    except Exception as e:
        print(e)
        sleep(randint(30,300))

        