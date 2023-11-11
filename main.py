from telebot import types
import telebot
bot = telebot.TeleBot(token='6513209707:AAHtT4PwyCfjHMPEE7OXsxTViHgD-DibYlg')
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    welcome_massage = "Добро пожаловать! Я ваш Telegram бот"
    availabe_commands = ' /start - Начать\n/help - Помощь'

    bot.send_message(user_id, welcome_massage + availabe_commands)
@bot.message_handler(commands=['help'])

def help(message):
    user_id = message.chat.id
    help_text = "Выберите действие:"
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Узнать новости")
    button2 = types.KeyboardButton("Узнать погоду")
    button3 = types.KeyboardButton("узнать мероприятия")
    marcup.row(button1, button2)
    marcup.row(button3)
    bot.send_message(user_id, help_text, reply_markup=marcup)

bot.polling(none_stop=True)