import telebot
import random
from telebot.types import Message

TOKEN = '583885451:AAFNXpsPeAbt8dNLwwuKoYwhSdopzb8KVSY'
bot = telebot.TeleBot(TOKEN)
ADDSTICK = False
ADMINS = []
ADDADMIN = False
REQV_USERS = ['test']
CREATOR_ID = '564932461'
CREATOR_NAME = 'bit6tream'
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
def command_start(message: Message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть\nНапиши /help чтобы получить справку')
    print(message.from_user.id)

@bot.message_handler(commands=['help'])
def command_help(message: Message):
    bot.send_message(message.chat.id, 'Итак, вот твой чек:\n /start - для начала\n /help - помощь\n /getstat -  получить статистику\n /addsticker - добавить стикер в пресет\n')

@bot.message_handler(commands=['hello'])
def command_hello(message: Message):
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)

#TODO
@bot.message_handler(commands=['requestadmin'])
def command_requestadmin(message: Message):
    if str(message.from_user.id) == CREATOR_ID:
        bot.send_message(message.chat.id, 'Ты меня создал\nКакой /requestadmin ?')
    else:
        bot.send_message(message.chat.id, 'Ожидайте одобрения от одного из управленцев...')
        bot.send_message(CREATOR, f'Заявка в админы от @{message.from_user.username}  \nДля одобрения отправь /setadmin')
        REQV_USERS.append(message.from_user.username)

@bot.message_handler(commands=['setadmin'])
def command_setadmin(message: Message):
    global ADDADMIN
    if str(message.from_user.id) == CREATOR_ID:
        USER_LIST = ''
        for i in range(0,len(REQV_USERS)):
            USER_LIST += str(REQV_USERS[i]) + '\n'
        bot.send_message(message.chat.id, f'Выбери username из списка:\n{USER_LIST}')
        ADDADMIN = True
        return
       



@bot.message_handler(commands=['adminlist'])
def command_adminlist(message: Message):
    bot.send_message(message.chat.id, ADMINS)

@bot.message_handler(commands=['getstat'])
def command_getstat(message: Message):
    bot.reply_to(message, 'В процессе...')

@bot.message_handler(commands=['addsticker'])
def command_addsticker(message: Message):
    global ADDSTICK
    # bot.reply_to(message, 'В процессе...')
    bot.send_message(message.chat.id, 'Отправь мне свой стикер')
    ADDSTICK = True

@bot.message_handler(commands=['stickbomb'])
def command_stickbomb(message: Message):
    i = 100
    while i > 0:
        bot.send_sticker(message.chat.id, random.choice(STICKERS))
        i -= 1

@bot.message_handler(commands=['ddos'])
def command_stickbomb(message: Message):
    i = 1000
    while i > 0:
        bot.send_sticker(message.chat.id, random.choice(STICKERS))
        bot.send_message(message.chat.id, 'DDOS')
        i -= 1

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    global ADDADMIN
    if message.from_user.id not in USERS:
        USERS.add(message.from_user.id)
    if str(message.from_user.id) == CREATOR_ID:
         if ADDADMIN == True:
            if str(message.text) in REQV_USERS:
                ADMINS.append(str(message.text))
                bot.send_message(message.chat.id, 'Пользователь добавлен в администраторы')
                ADDADMIN = False
            else:
                bot.send_message(message.chat.id, 'Заявки от такого пользователя не приходило')
    print(message)

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