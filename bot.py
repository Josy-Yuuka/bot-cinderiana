from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message = "Fala, mofih " + update.message.from_user.first_name + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():

    token = '1397244422:AAEqemqlKSMGlqGxCcdWJpTHwWch9_J6pXs'

    updater = Updater (token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print('to funfando mamazita' + str(updater))
    updater.idle()

if __name__ == '__main__':
        main()