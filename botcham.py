import telebot


Token = "5773060087:AAHpLmsAqn4b8eIQaL997SX85N7wRE5R2WQ"


bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Assalomu alaykum hurmatli ...(name)...")


bot.polling(none_stop=True)

