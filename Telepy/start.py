import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot("6327341872:AAHiyzLEb_55R5FzOdWga3miCAHH_J3Jycg")


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	key = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 	button1 = types.KeyboardButton("Download Movie")
# 	key.add(button1)
# 	bot.send_message(message.chat.id, "Hello, {0.first_name}. I'm {1.first_name}.".format(message.from_user, bot.get_me()), parse_mode="html", reply_markup=key)
	
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # buttons
    keyboard.row('🎥Download Video', '🎵Download Audio')
    keyboard.row('📄Download Video Playlist', '📄Download Audio Playlist')
    bot.send_message(
        message.chat.id, """Вітаю, {0.first_name}!\nНатисніть відповідну кнопку 👇 щоб отримати інформацію.{}\n\n(примітка, для того щоб відобразилась повна назва кнопки, переверніть свій смартфон в горизонтальне положення для автоматичного повороту зображення на екрані (для користувачів з невеликими екранами))""" .format(message.from_user, bot.get_my_description), reply_markup=keyboard)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	

bot.polling()