from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

# Replace with your bot token
BOT_TOKEN = "7735565121:AAF6jkjRPsmsEZdlCRQbRPAcMtF_tNXj-WA"

# WebApp URL
WEBAPP_URL = "https://testing-production-1515.up.railway.app"

def start(update: Update, context: CallbackContext):
    """Send an inline keyboard with a WebApp button."""
    chat_id = update.effective_chat.id
    keyboard = [
        [
            InlineKeyboardButton(
                text="Authenticate with WebApp",
                web_app={"url": WEBAPP_URL}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id, text="Click the button below to authenticate:", reply_markup=reply_markup)

def main():
    """Start the bot."""
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Register command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start polling for updates
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    print("Bot is running...")
    main()
