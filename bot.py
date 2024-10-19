import telebot, random
from my_token import TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['rand'])
def send_bye(message):
    bot.reply_to(message, random.randint(1,10))

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "h" * count_heh)

@bot.message_handler(commands=['game'])
def send_keys(msg):
    bot.send_message(msg.chat.id, 'Выбери кнопку', reply_markup=gen_markup())

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton("🔥", callback_data="1"),
        InlineKeyboardButton("🔥", callback_data="2"),
        InlineKeyboardButton("🔥", callback_data="3"),
        InlineKeyboardButton("🔥", callback_data="4"),
        InlineKeyboardButton("🔥", callback_data="5"),
        InlineKeyboardButton("🔥", callback_data="6"))
    return markup
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == str(random.randint(1, 6)):
        bot.answer_callback_query(call.id, "Ты выиграл", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "Ты проиграл", show_alert=True)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if 'привет' in message.text:
        bot.reply_to(message, 'Пока')
    bot.reply_to(message, message.text)
    
bot.polling()
