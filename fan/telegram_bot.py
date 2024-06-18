import telebot
from telebot import types
import telegram_bot_files


bot = telebot.TeleBot('7257644702:AAHdSn_oYhpexlcCghbylnLoSEE2xxefBdo')
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
for rarest in telegram_bot_files.rarest:
    button = types.KeyboardButton(rarest)
    start_keyboard.add(button)


@bot.message_handler(commands=['start'])
def start_bot(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, text=f'Hello {message.from_user.first_name}, it\'s bot of game '
                                               f'\'\'Brawl Stars\'\'', reply_markup=start_keyboard)


@bot.message_handler(content_types=['text'])
def get_rarest(message):
    rarest_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for rarest_brawlers, brawlers in telegram_bot_files.rarest.items():
        if message.text == rarest_brawlers:
            for brawler in brawlers:
                rarest_keyboard.add(brawler)
    bot.send_message(message.chat.id, text='Its all brawlers in this rarest',
                     reply_markup=rarest_keyboard)


bot.infinity_polling()































































































