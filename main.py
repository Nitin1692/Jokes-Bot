import os
from dotenv import load_dotenv
import telebot

import pyjokes as py


load_dotenv()
API_KEY = os.getenv('API_KEY')
bot =telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Joke'])
def print_joke(message):
   a = py.get_joke()
   bot.send_message(message.chat.id, a)


@bot.message_handler(commands=['Start'])
def start_command(message):
    a= "Hello and welcome to Random joke Generator! Select one of the commands below to get started.(Please note, all the jokes are programming-related jokes, so don't be offended if you don't get some of them."
    bot.send_message(message.chat.id, a)

bot.polling()