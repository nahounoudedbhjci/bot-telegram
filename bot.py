import telebot

TOKEN = 8012584916:AAHhaN1s6v2gBWv9OU8ew0vAN3tye0Jal6U
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bienvenue sur BIG, le bot intelligent !")

bot.polling()
