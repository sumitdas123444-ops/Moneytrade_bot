import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Guru Trader Bot!\n\n"
        "💰 Invest with confidence.\n\n"
        "Commands:\n"
        "/invest - Investment Details\n"
        "/payment - Payment UPI\n"
        "/support - Contact Admin"
    )

async def invest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Investment Process\n\n"
        "1. Minimum Investment: ₹500\n"
        "2. Send payment using /payment\n"
        "3. Send payment screenshot to admin\n"
        "4. Profit will be shared after trade."
    )

async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Payment Details\n\n"
        "UPI ID:\n"
        "7086113334@ptyes\n\n"
        "Payment ke baad screenshot @ssuuumitt ko bhej dijiye."
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Admin Support:\n@ssuuumitt"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("invest", invest))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CommandHandler("support", support))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
