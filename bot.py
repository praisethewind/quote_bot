import telebot
from telebot import types
from random import randint
import json

bot = telebot.TeleBot('6020189587:AAFoNYpOMjWqjhcS9AL9VsWoH3rXhUzBfXY')

replies = [
    '🔥 Показать мотивационную цитату',
    '😉 Еще',
    '😇 Еще одну',
    '😏 Еще одна и я пойду',
    '😈 Точно последняя!',
]

quotes_emoji = [
    '✍️',
    '😳',
    '🤑',
    '🧐',
    '🥸',
    '☝️',
    '🧠',
    '🫵',
    '👐',
    '🌊',
    '🧘‍♂',
    '🗿',
    '💫',
    '👁',
    '💪',
    '🤝',
    '🤑',
    '👌',
    '💥',
    '🏃',
    '🧗',
    '☯️',
]

quotes_file = open('quotes.json', encoding='utf-8')

quotes = json.load(quotes_file)

quotes_file.close()

def get_rand_quote():
    return quotes_emoji[randint(0, len(quotes_emoji))] + " " + quotes[randint(0, len(quotes))]

def send_message(user_id, reply_index):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(replies[reply_index])
    markup.add(btn)
    bot.send_message(user_id, get_rand_quote(), reply_markup=markup)   

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(replies[0])
    markup.add(btn)
    bot.send_message(message.from_user.id, "👋 Привет, этот бот может поддержать тебя мотивационной цитатой", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    user_id = message.from_user.id
    try:
        reply_index = replies.index(text) + 1
        if reply_index >= len(replies):
            reply_index = 0

        send_message(user_id, reply_index=reply_index)
    except ValueError:
        pass
    

bot.polling(none_stop=True, interval=0)
