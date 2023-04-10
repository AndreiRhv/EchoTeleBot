import telebot
# Greate the Bot
bot = telebot.TeleBot('5865014325:AAGIyMvXiWGFX3W5YhQZdjcVyXf-IbkR-ec')
# Command processing function START
@bot.message_handler(commands=["start"])
def start(m, res=False):bot.send_message(m.chat.id, 'Iam here. Text me samething')
# Receiving messages from USER
@bot.message_handler(content_types=["text"])
def handle_text(message):bot.send_message(message.chat.id, 'You wrote:' +message.text)
# Start the Bot
bot.polling(none_stop=True, interval=0)


