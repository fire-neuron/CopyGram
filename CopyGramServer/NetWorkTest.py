import TeleBot
import Initializer
settings = Initializer.settings
token = settings['telegram']['token']
bot = TeleBot.TeleBot(token)
result = bot.CheckBot()
print(result)
