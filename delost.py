import telebot
import random
import pickle
from telebot.types import Message

TOKEN = '583885451:AAFNXpsPeAbt8dNLwwuKoYwhSdopzb8KVSY'
bot = telebot.TeleBot(TOKEN)
ADDSTICK = False
STICKERS = ['CAADAgADHwADa-18CnJ6NnqU84-1Ag',
            'CAADAgADyQEAAtvnDQAB19KJ0eCiO5cC',
            'CAADAgADVQAD6kb8ECvohJYCchf_Ag',
            'CAADAgADHQADDsfGGwjRP62OEBzyAg',
            'CAADAgADOwADTb8jFXBEE145HDxvAg',
            'CAADBAADNgMAAkMxogbz14tgzIphyAI',
            'CAADBAADOAMAAkMxogY0MyjNcMGAOQI',
            'CAADAgADrwADTptkAoftMsdli6fnAg',
            'CAADAgADsAADTptkAler0GVnHyzGAg',
            'CAADAgADPQAD1VqSFWqk3-GgIldHAg',
            'CAADAgADCwADNMoRCrsTCJDTmPU1Ag',
            'CAADAQADhwEAAjqtBAUdAR6f6eANlwI']
USERS = set()
@bot.message_handler(commands=['start'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть\nНапиши /help чтобы получить справку')

@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'Итак, вот твой чек:\n /start - для начала\n /help - помощь\n /getstat -  получить статистику\n /addsticker - добавить стикер в пресет\n')

@bot.message_handler(commands=['hello'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)

@bot.message_handler(commands=['getstat'])
def command_handler(message: Message):
    bot.reply_to(message, 'В процессе...')

@bot.message_handler(commands=['addsticker'])
def command_handler(message: Message):
    global ADDSTICK
    # bot.reply_to(message, 'В процессе...')
    bot.send_message(message.chat.id, 'Отправь мне свой стикер')
    ADDSTICK = True

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    if message.from_user.id not in USERS:
        USERS.add(message.from_user.id)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    global ADDSTICK

    if (ADDSTICK == True) :
        STICKERS.append(message.sticker.file_id)
        bot.send_message(message.chat.id, 'Твой стикер добавлен успешно')
        ADDSTICK = False
    else:
        bot.send_sticker(message.chat.id, random.choice(STICKERS))
    # print(message.sticker.file_id)
    # bot.send_message(message.chat.id,message.sticker)


bot.polling(timeout=60)
#@bot.edited_message_handler(content_types=['text'])
