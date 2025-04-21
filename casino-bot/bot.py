
import telebot
from telebot import types

bot = telebot.TeleBot("7701797337:AAGCwk15d17a2v8RslBtvOLIJDOSm2eEdO0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🎲 Крутить рулетку", url="https://your-name.github.io/casino-bot/roulette.html")
    button2 = types.InlineKeyboardButton("🎁 Получить бонус", url="https://your-bonus-link.com")
    markup.add(button1)
    markup.add(button2)

    with open("static/banner.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🎰 Добро пожаловать в Казино!
💥 500% к первому депозиту + 75 фриспинов!", reply_markup=markup)

bot.polling()
