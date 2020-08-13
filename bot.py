from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from numpy.core.defchararray import lower

STATE1 = 1
STATE2 = 2

def inputAssunto(update, context):
    message = "pau no cu do coronga :*"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def welcome(update, context):
    message = "Fala, mofih " + update.message.from_user.first_name + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def beleza(update, context):
    message = '''já passou alquinho na mão?\n
                1 - Sim         2 - não'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def inputBeleza(update, context):
    feedback = lower(update.message.text)
    print(beleza)
    if (beleza == 1 or 'sim'):
            message = """ui ui ui 
                    \n bate aqui então o/
                    \n heeey.. eu tbm passei alquinho"""
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return STATE2
    else:
        if (beleza == 2 or 'não'):
             message = '''vira a mãozinha, vou passar alquinho!
                        \n puff puff
                        \n agora ta limpinha'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

def main():

    token = '1397244422:AAEqemqlKSMGlqGxCcdWJpTHwWch9_J6pXs'

    updater = Updater (token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('beleza', beleza)],
        states={
            STATE1: [MessageHandler(Filters.text, inputBeleza)],
            STATE2: [MessageHandler(Filters.text, inputAssunto)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    print('to funfando mamazita' + str(updater))
    updater.idle()

if __name__ == '__main__':
        main()
