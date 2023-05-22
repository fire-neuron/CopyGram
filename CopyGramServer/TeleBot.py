import urllib.request
import urllib.parse
import  json

class TeleBot():
    def __init__(self, token):
        self.BOT_TOKEN = token
    def send_message(self, chat_id, message):
        CHAT_ID = chat_id
        MESSAGE = message
        url = 'https://api.telegram.org/bot' + self.BOT_TOKEN + '/sendMessage'
        data = {
            'chat_id': CHAT_ID,
            'text': MESSAGE}
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url, data)
        try:
            response = urllib.request.urlopen(req)

        except urllib.error.HTTPError as e:

            if e.code == 403:
                print('HTTP Error 403: Forbidden, please, unlock telegram bot')


    def CheckBot(self):

        url = 'https://api.telegram.org/bot' + self.BOT_TOKEN + '/getMe'
        # Создаем объект Request с URL и методом POST
        try:
            req = urllib.request.Request(url, method='POST')
            # Открываем URL и получаем объект Response
            with urllib.request.urlopen(req) as response:
                # Читаем содержимое ответа как байты
                result = response.read()
                # Декодируем байты в строку JSON
                result = result.decode('utf-8')
                # Преобразуем строку JSON в объект Python
                result = json.loads(result)
                # Выводим результат запроса
                return str(result['ok'])
        except urllib.error.HTTPError as e:

            if e.code == 401:
                return 'Unauthorized'
        except:
            return "NotConnect"

        





