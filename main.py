import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 Вставь свои ключи
TELEGRAM_TOKEN = "8239319316:AAHx1y5XjkAeI3BQpAGGajg_T6yZnoBrDJU"
GEMINI_API_KEY = "AIzaSyDFokhW_q-zImDkV_9YeNde6F-fmFFCPIo"

# Настройка Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот на Gemini. Напиши мне сообщение 🙂")

# Ответ на текст
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = model.generate_content(user_message)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Бот запущен 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
