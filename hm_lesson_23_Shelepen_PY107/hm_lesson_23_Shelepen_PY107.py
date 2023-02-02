from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot_tok  # импортируем файл config
import logging
import keyboard

storage = MemoryStorage()
# создаем бот
bot = Bot(bot_tok, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
                           u'[%(asctime)s] %(message)s')

poem_winter = """Белая береза под моим окном
Принакрылась снегом, точно серебром.
На пушистых ветках снежною каймой
Распустились кисти белой бахромой.
И стоит береза в сонной тишине,
И горят снежинки в золотом огне.
А заря, лениво, обходя кругом,
Обсыпает ветки новым серебром.

Сергей Есенин"""

poem_summer = """

Вот
И лето на пороге:
Реют пчелы-недотроги,
Величаво карауля
Привлекательные ульи,
Чтобы всякие тревоги
Потонули в мерном гуле,
Как набаты тонут в благовесте,
И в июне,
И в июле,
И в особенности
В августе.
Леонид Мартынов"""

poem_spring = """Травка зеленеет,
Солнышко блестит;
Ласточка с весною
В сени к нам летит.

С нею солнце краше
И весна милей…
Прощебечь с дороги
Нам привет скорей!

Дам тебе я зерен,
А ты песню спой,
Что из стран далеких
Принесла с собой…
Алексей Плещеев"""

poem_autumn = """Унылая пора! Очей очарованье!
Приятна мне твоя прощальная краса —
Люблю я пышное природы увяданье,
В багрец и в золото одетые леса,
В их сенях ветра шум и свежее дыханье,
И мглой волнистою покрыты небеса,
И редкий солнца луч, и первые морозы,
И отдаленные седой зимы угрозы.
Александр Пушкин"""


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Выбирай',
                           reply_markup=keyboard.start_kb, parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def smile(message: types.Message):
    if message.text == 'Зима':
        await bot.send_photo(chat_id=message.chat.id, photo=open("winter.png", "rb"))
        await bot.send_message(chat_id=message.chat.id, text=poem_winter,
                               parse_mode='Markdown')
    elif message.text == 'Весна':
        await bot.send_photo(chat_id=message.chat.id, photo=open("spring.png", "rb"))
        await bot.send_message(chat_id=message.chat.id, text=poem_spring,
                               parse_mode='Markdown')
    #
    elif message.text == 'Лето':
        await bot.send_photo(chat_id=message.chat.id, photo=open("summer.png", "rb"))
        await bot.send_message(chat_id=message.chat.id, text=poem_summer,
                               parse_mode='Markdown')

    else:
        await bot.send_photo(chat_id=message.chat.id, photo=open("autumn.png", "rb"))
        await bot.send_message(chat_id=message.chat.id, text=poem_autumn,
                               parse_mode='Markdown')
    await bot.send_message(chat_id=message.chat.id, text="Понравилось?",
                           reply_markup=keyboard.kb_time, parse_mode='Markdown')


@dp.callback_query_handler(text_contains="like")
async def like(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text="😊",
                           reply_markup=keyboard.start_kb)


@dp.callback_query_handler(text_contains="no")
async def dislike(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text="😢",
                           reply_markup=keyboard.start_kb)


if __name__ == "__main__":
    print("Привет! Я Бот и я готов к работе!")
    executor.start_polling(dp, skip_updates=True)
