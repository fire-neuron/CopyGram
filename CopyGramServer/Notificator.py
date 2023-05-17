# -*- coding: utf-8 -*-
import TeleBot
import Initializer
import RepGen

settings = Initializer.settings

token = settings['telegram']['token']
users_id = settings['telegram']['recipients']
path_to_advanced_report = Initializer.path_to_advanced_report


def connect_tg():
    bot = TeleBot.TeleBot(token)
    return bot


def horn():
    bot = connect_tg()
    for user in users_id:
        bot.send_message(user, RepGen.Report_Maker('Messenger'))


if __name__ == "__main__":
    horn()
