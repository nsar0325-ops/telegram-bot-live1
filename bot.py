from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("8572772636:AAHzNKW8WQFcN9kC4-Zm7gzZOtsUkzRZFDU")
ADMIN_ID = 8301795891
LINK = "https://verifytg.org/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else "NoUsername"

    keyboard = [
        [InlineKeyboardButton("Open verifytg.org", callback_data="open_link")]
    ]

    await update.message.reply_text(
        text="Click here to browse the telegram accounts:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📢 /start սեղմեց\nUser ID: {user.id}\nUsername: {username}"
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    username = f"@{user.username}" if user.username else "NoUsername"

    await query.answer()
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"⚠️ Սեղմեց կոճակը\nUser ID: {user.id}\nUsername: {username}"
    )

    await query.edit_message_text(f"Here is your link: {LINK}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("✅ Bot started successfully!")
    app.run_polling()

if __name__ == "__main__":
    main()

