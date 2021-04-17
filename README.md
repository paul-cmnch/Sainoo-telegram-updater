# Sainoo-telegram-updater
A Telegram bot that will automatically send updates about new job postings on Sainoo

# Deployment
- Add the files in your server
- Install the python-telegram-bot module using pip
- In the file config.py, enter the bot token that was generated through BotFather
- Start the sainoo_telegram_handler.py script (will continue to work in the background, you may want to automatically start the script at server reboot)
- Set-up a cron job to start the sainoo_main.py script at a regular interval
