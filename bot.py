import os
from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import Application, Updater, CommandHandler, CallbackContext, MessageHandler, filters, ContextTypes
import aiohttp

# Load .env variables

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def getSubmissions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get total leetcode submissions when the command / getSubmissions is issued"""
    url=f"http://localhost:3000/Jeryl01/solved"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            data = await resp.json()
    # 2. Extract the solved count
    solved = data.get("solvedProblem", 0)
    # 3. Send back to the user
    await update.message.reply_text(f"You’ve solved {solved} problems on LeetCode!")

    

def main():
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("getSubmissions", getSubmissions))

    # on non command i.e message - echo the message on Telegram
    

    # Run the bot until the user presses Ctrl-C
    print("Polling for mesages! Press ctrl+c to exit")
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    

if __name__ == "__main__":
    main()