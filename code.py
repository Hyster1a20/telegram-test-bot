import os
import telebot

tk = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(tk)

@bot.message_handler(commands=['start', 'alo'])
def send_welcome(message):
    bot.reply_to(message, "u're in! ")
