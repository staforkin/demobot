import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#442705619:AAFpWEB5292Mf2Sy4PYYrwHdbI-jV4Y_jso
updater = Updater(token='442705619:AAFpWEB5292Mf2Sy4PYYrwHdbI-jV4Y_jso', request_kwargs={
    'proxy_url': 'socks5://145.239.0.192:1080/'
})
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()