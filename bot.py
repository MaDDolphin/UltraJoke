import telebot
import rand_joke

bot = telebot.TeleBot('token');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text, ' ', message.from_user.first_name)
    test = open('log.txt', 'a')
    test.write(message.text + ' ' + message.from_user.first_name + ' \n')
    test.close()
    if message.text == "/help" or message.text == "/help@UltraJoke_bot":
        bot.send_message(message.chat.id,
                         "Это просто бот с анекдотами. Нажми /rand чтоб получить свой, или /rand_sound чтоб послушать")
    elif message.text == "/rand" or message.text == "/rand@UltraJoke_bot":
        bot.send_message(message.chat.id, rand_joke.random_joke())
    elif message.text == '/rand_sound' or message.text == '/rand_sound@UltraJoke_bot':
        bot.send_audio(message.chat.id, audio=open(rand_joke.speach_joke(), 'rb'))
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

