import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to MoneyTrade Bot!\n\n"
        "Use:\n"
        "/buy - Buy Plan\n"
        "/help - Contact Admin"
    )

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Payment Details\n\n"
        "UPI ID: yourupi@upi\n\n"
        "Payment ke baad screenshot admin ko bhej do."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Admin: @yourusername"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("help", help_command))

print("Bot Started")
app.run_polling()
