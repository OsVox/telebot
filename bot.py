import telebot

admin_id = 244917904
address = 461449438

bot = telebot.TeleBot('5145009955:AAGCxw_7dlusVqB8evXRNd1qppX1V1-RQMo')


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id != admin_id:
        bot.send_message(message.chat.id, 'Привет! Напишите сообщение и мы его передадим куда надо!')


@bot.message_handler()
def get_user_message(message):
    global address
    if message.chat.id != admin_id:
        bot.send_message(message.chat.id, 'Сообщение идёт куда надо... Вы можете написать ещё.')
        bot.send_message(admin_id, f'Cообщение от: @{message.from_user.username}, ID для ответа: {message.chat.id}\n\n{message.text}')
    else:
        if message.text[:10] == '/change_to':
            if len(message.text[11:].rstrip(' ')) == 9:
                address = int(message.text[11:])
                bot.send_message(admin_id, f'поменял адресата на {message.text[11:]}')
            else:
                bot.send_message(admin_id, 'ID состоит из 9 цифр')
        else:
            bot.send_message(address, message.text)


while True:
    try:
        bot.polling(none_stop=True)
    except:
        pass
