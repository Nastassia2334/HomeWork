import logging

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

import config

storage = MemoryStorage()
bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(filename='log.txt',
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    )


class Text_user(StatesGroup):
    text = State()
    answer = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = KeyboardButton("Привет")
but2 = KeyboardButton("Отправить фото")
kb.add(but1)
kb.add(but2)


@dp.message_handler(commands=["start"])
async def start_commands(message: types.Message):
    await bot.send_message(message.chat.id, text="Бот запущен!", reply_markup=kb, parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def text_commands(message: types.Message):
    if message.text == "Привет":
        await bot.send_message(message.chat.id, text=f"привет {message.from_user.first_name}!",
                               parse_mode='Markdown')

    if message.text == "Отправить фото":
        await message.answer("Давайте добавим фото")


@dp.message_handler(content_types=['photo'], state=None)
async def photo_add(message: types.Message):
    await message.answer("Сохранить? ")
    await Text_user.text.set()
    photo = message.photo.pop()
    await photo.download()


@dp.message_handler(state=Text_user.text)
async def text_photos(message: types.Message, state: FSMContext):
    if message.text == 'да':
        await message.answer('давайте подпишем фото')
        await Text_user.answer.set()
    else:
        await message.answer(" Не сохранено ")
        await state.finish()


@dp.message_handler(state=Text_user.answer)
async def text_answer(message: types.Message, state: FSMContext):
    message_text = message.text
    await state.update_data(message_text=message_text)
    await message.answer("Ваше фото с записью сохранены")
    await state.finish()


if __name__ == "__main__":
    print('Бот запущен!')
    executor.start_polling(dp, skip_updates=True)
