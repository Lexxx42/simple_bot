from bot_commands import *

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
