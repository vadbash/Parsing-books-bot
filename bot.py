import telebot
import requests
from config import telegram_bot_token as token

bot = telebot.TeleBot(token)
    
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, text="Hello, it's my bot")

# https://www.epubbooks.com/book/547-innocents
bot.polling()