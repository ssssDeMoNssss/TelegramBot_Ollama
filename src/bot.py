import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import ollama

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я бот для работы с OLLAMA.')

# Обработчик текстовых сообщений
def echo(update: Update, context: CallbackContext):
    response = ollama.generate(model='llama2', prompt=update.message.text)
    update.message.reply_text(f"OLLAMA: {response['response']}")

# Регистрация обработчиков
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

if __name__ == "__main__":
    print("Бот запущен!")
    updater.start_polling()
    updater.idle()