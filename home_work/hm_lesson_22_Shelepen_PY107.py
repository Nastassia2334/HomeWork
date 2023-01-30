from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot_tok  # импортируем файл config
#создаем бот
bot = Bot(bot_tok)
dp = Dispatcher(bot)
#создаем inlineкнопки
inline_kb = InlineKeyboardMarkup()
inline_kb_info = InlineKeyboardButton(text="Информация о Python",
                                      url='https://ru.wikipedia.org/wiki/Python')
inline_kb_list = InlineKeyboardButton(text="Cписок полезной литературы",
                                      url='https://zavistnik.com/7-luchshih-knig-po-python/')
inline_kb.add(inline_kb_info, inline_kb_list)


@dp.message_handler(commands=['start'])
async def info_button(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Добро пожаловать!",
                           reply_markup=inline_kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
