import json
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from config import Bot_token


def start(update: Update, _: CallbackContext) -> None:
    keyboard = [[telegram.KeyboardButton('/stop')]]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    user = update.effective_user
    with open('/home/paul/Python_projects/sainoo_active_users.json', 'r') as f:
        active_users = json.load(f)
    if update.message.chat_id not in active_users:
        active_users.append(update.message.chat_id)
        with open('/home/paul/Python_projects/sainoo_active_users.json', 'w') as f:
            json.dump(active_users, f)

    update.message.reply_markdown_v2(
        fr'Hello {user.mention_markdown_v2()}\! You will receive updates when new Sainoo postings appear\.',
        reply_markup=reply_markup
    )


def stop(update: Update, _: CallbackContext) -> None:
    keyboard = [['/start']]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    with open('/home/paul/Python_projects/sainoo_active_users.json', 'r') as f:
        active_users = json.load(f)
    if update.message.chat_id in active_users:
        active_users.remove(update.message.chat_id)
        with open('/home/paul/Python_projects/sainoo_active_users.json', 'w') as f:
            json.dump(active_users, f)
    update.message.reply_markdown_v2(
        fr'You are no longer subscribed to Sainoo updates\.',
        reply_markup=reply_markup)


def unknown_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(f"'{update.message.text}' is not a recognised command.")


def main() -> None:
    updater = Updater(Bot_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown_command))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
