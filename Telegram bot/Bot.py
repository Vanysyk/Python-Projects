import telebot
import sqlite3
import bd_io
import math_module_io
import config


bot = telebot.TeleBot(config.bot_id)


def show_log(message):
    s = (message.content_type + ' | ' + message.from_user.first_name + ' :')
    if message.content_type == 'text':
        s += ' ' + message.text
    elif message.content_type == 'audio':
        s += 'Аудиофайл ' + str(message.json['audio']['file_name']) + ', длительность : ' + str(message.audio.duration) + ' секунд'
    print(s)

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    print(message.from_user.first_name)
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    show_commands(message)

@bot.message_handler(commands=['test'])
def test(message):
    pass

@bot.message_handler(content_types=['text'])
def text(message):
    show_log(message)
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('ъуъ', 'ъ!')
    # bot.send_message(message.chat.id, 'ыть')
    bot.send_message(message.chat.id, 'ыть!', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == '1':
        answer = 'Хорошо'
    elif call.data == '2':
        answer = 'Не особо'
    elif call.data == '3':
        answer = 'Плохо'

    bot.send_message(call.message.chat.id, answer)


    # print(message.from_user.first_name)
    # bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    # show_commands(message)

@bot.message_handler(commands=['cmd'])
def show_commands(message):
    bot.send_message(message.chat.id, '*список команд*')


@bot.message_handler(content_types=['audio'])
def test_audio(message):
    show_log(message)
    if message.audio.duration < 10:
        file = bot.get_file(message.audio.file_id)
        a = bot.download_file(file.file_path)
        # f = open(message.json['audio']['file_name'], "wb")
        # f.write(a)
        # f.close()
        bot.send_message(message.chat.id, 'Принимаем')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Хорошо', callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='Так себе', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='Плохо', callback_data=3))
        bot.send_message(message.chat.id, text="Как тебе наше приложение?", reply_markup=markup)
        bd_io.create_new_record(message.from_user.id, file.file_path)
        markup = 0;
    else:
        bot.send_message(message.chat.id, 'Переделывай')





bot.polling(none_stop=True, interval=5)
