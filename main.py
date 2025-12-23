import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a user to ban.")
        return
    await update.message.chat.ban_member(
        update.message.reply_to_message.from_user.id
    )
    await update.message.reply_text("User banned.")

async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a user to unban.")
        return
    await update.message.chat.unban_member(
        update.message.reply_to_message.from_user.id
    )
    await update.message.reply_text("User unbanned.")

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a user to mute.")
        return
    await update.message.chat.restrict_member(
        update.message.reply_to_message.from_user.id,
        permissions={}
    )
    await update.message.reply_text("User muted.")

app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("unban", unban))
app.add_handler(CommandHandler("mute", mute))

app.run_polling()
