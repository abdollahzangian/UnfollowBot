from instabot import Bot
from time import sleep
from random import randint
import config

bot = Bot()

def login():
    bot.login(username=config.username, password=config.password, ask_for_code=True)

def get_fallowers():
    for target in config.target_users:
        users = bot.get_user_followers(target)
        for user in users:
            try:
                bot.follow(user)
                sleep(randint(6,20))
            except Exception as e:
                print(e)
                sleep(randint(30,300))

