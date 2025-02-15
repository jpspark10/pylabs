from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, Application
from python_translator import Translator
from config import BOT_TOKEN


async def start(update, context):
    keyboard = [['/change']]
    mark = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False, resize_keyboard=True)
    context.user_data['from'] = 'russian'
    context.user_data['to'] = 'english'

    await update.message.reply_text(
        f'Текущее направление перевода: '
        f'\n{context.user_data['from']} -> {context.user_data['to']}'
        '\n(смена направления перевода: /change)',
        reply_markup=mark
    )
    await update.message.reply_text('Введите текст для перевода:', disable_notification=True)


async def change(update, context):
    print(f'{context.user_data['from']} -> {context.user_data['to']}')

    context.user_data['buffer'] = context.user_data['from']
    context.user_data['from'] = context.user_data['to']
    context.user_data['to'] = context.user_data['buffer']
    context.user_data['buffer'] = None

    await update.message.reply_text('Направление было изменено!'
                                    f'\nТекущее направление перевода: '
                                    f'\n{context.user_data['from']} -> {context.user_data['to']}')

    print(f'{context.user_data['from']} -> {context.user_data['to']}')


async def translate(update, context):
    translator = Translator()
    context.user_data['sentence'] = update.message.text
    await update.message.reply_text(
        f'{translator.translate(context.user_data['sentence'], context.user_data['to'], context.user_data['from'])}'
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("change", change))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

    application.run_polling()


if __name__ == '__main__':
    main()
