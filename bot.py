from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from gpt import ask_gpt

# Храни историю диалога (упрощённо)
user_history = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    text = update.message.text

    # Инициализируем историю
    if user_id not in user_history:
        user_history[user_id] = [{"role": "system", "content": "Ты поддерживающий психолог. Отвечай с эмпатией."}]

    # Добавляем сообщение пользователя
    user_history[user_id].append({"role": "user", "content": text})

    # Получаем ответ от GPT
    reply = ask_gpt(user_history[user_id])
    user_history[user_id].append({"role": "assistant", "content": reply})

    await update.message.reply_text(reply)

# Запуск бота
if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
