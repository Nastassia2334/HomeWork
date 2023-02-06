from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
import os
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config  # импортируем файл config
import keyboard  # импортируем файл config keyboard

import logging  # модуль для вызова информации

list_photo = []
# хранилище MemoryStore
storage = MemoryStorage()  # FSM
bot = Bot(token=config.tok, parse_mode=types.ParseMode.HTML)  # pars_mode станавливает режим парсинг сообщении бота;
# инициализируем диспетчер к нашему боту
dp = Dispatcher(bot, storage=storage)  # хранилище состояний в оперативной памяти
# включаем логирование
logging.basicConfig(filename='log.txt',
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    )


class meinfo(StatesGroup):
    Q1 = State()
    Q2 = State()


@dp.message_handler(Command("me"), state=None)  # создадим команду me для админа
async def enter_meinfo(message: types.Message):
    if message.chat.id == config.admin:
        await message.answer("начинаем настройку.\n"
                             "№1 Введите линк на ваш профиль")
        await meinfo.Q1.set()


@dp.message_handler(state=meinfo.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)

    await message.answer("Линк сохраненю \n"
                         "№2 Введите текст.")
    await meinfo.Q2.set()


@dp.message_handler(state=meinfo.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)

    await message.answer("Текст сохранен.")

    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")

    joinedFile = open("link.txt", "w", encoding="UTF-8")
    joinedFile.write(str(answer1))
    joinedFile = open("text.txt", "w", encoding="UTF-8")
    joinedFile.write(str(answer2))

    await message.answer(f'Ваша ссылка на профиль: {answer1}\nВаш текст:\n{answer2}')

    await state.finish()


# создаем handler на команду /Check me
# по сути мы указываем боту на какую команду будем реагировать
@dp.message_handler(Command("start"), state=None)
# после задаем функцию, которая отправит сообщение на заданную команду
async def welcome(message):
    # создаем файл в который будем записывать id пользователя
    joinedFile = open("user.txt", "r")
    joinedUsers = set()
    # цикл в котором проверяем имеется ли такой id в файле user
    for line in joinedFile:
        joinedUsers.add(line.strip())

    # делаем запись в файл user нового id
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id, f"ПРИВЕТ, *{message.from_user.first_name}*, БОТ РАБОТАЕТ",
                           reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(commands=['rassilka'])
async def rassilka(message: types.Message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Рассылка началась"
                                                f"\nБот оповестит когда рассылку закончит*", parse_mode='Markdown')
        receive_users, block_users = 0, 0
        joinedFile = open("user.txt", "r")
        joinedUsers = set()
        for line in joinedFile:
            joinedUsers.add(line.strip())
        joinedFile.close()
        for user in joinedUsers:
            try:
                await bot.send_photo(user, open('photo.png', 'rb', message.text[message.text.find(' '):]))
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)
        await bot.send_message(message.chat.id, f"*Рассылка была завершена*\n"
                                                f"получили сообщение:{receive_users}*\n"
                                                f"заблокировали бота: {block_users}*", parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
# после задаем функцию, которая оправит сообщение на заданную команду
async def get_message(message):
    if message.text == "Информация":
        await bot.send_message(message.chat.id, text="Информация\n Бот создан специально для обучения",
                               parse_mode='Markdown')

    if message.text == "Статистика":
        await bot.send_message(message.chat.id, text="Хочешь посмотреть статистику бота?", reply_markup=keyboard.stats,
                               parse_mode='Markdown')

    if message.text == "Разработчик":
        link1 = open("link.txt", encoding="utf-8")
        link = link1.read()

        text1 = open('text.txt', encoding="utf-8")
        text = text1.read()
        await bot.send_message(message.chat.id, text=f"Создатель: {link}\n{text}", parse_mode='Markdown')

    if message.text == "Покажи пользователя":
        await bot.send_message(message.chat.id, text="Хочешь посмотреть id бота?", reply_markup=keyboard.stats_user,
                               parse_mode='Markdown')

    if message.text == "Добавить фото":
        await message.answer("Давайте добавим фото в нашу галерею")

    if message.text == "Открыть фото из галереи":
        await message.answer("Загружаю фото")
        photo_list = os.listdir("photos")
        for photo in photo_list:
            photo = open("./photos/" + photo, "rb")
            await bot.send_photo(message.chat.id, photo)


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_add(message: types.Message):
    photo = message.photo.pop()

    await photo.download()
    await message.answer("фото добавлено")


@dp.callback_query_handler(text_contains='join')  # мы прописывали в кнопках теперь их ловим
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open('user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Вот статистика бота: *{d}* человек', parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Утебя нет админки\n Куда ты полез', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='cancle')
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'Ты вернулся в главное меню. Жми опять кнопки', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='user_id')
async def user_id(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'Номер id - {call.from_user.id}', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='deselected')
async def deselected(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Вы отменили выбор")


# создаем точку входа
if __name__ == "__main__":
    print('Бот запущен!')
    executor.start_polling(dp, skip_updates=True)
