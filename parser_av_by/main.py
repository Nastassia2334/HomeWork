import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from config import tokEn
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests
from bs4 import BeautifulSoup
import time

url = "https://cars.av.by/bmw/x6"
headers1 = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

storage = MemoryStorage()
bot = Bot(token=tokEn, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

list_bmw = []

kb = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = KeyboardButton("Все автомобили на сайте")
but2 = KeyboardButton("Объявления с первой страницы")
but3 = KeyboardButton("Всего объявлений на сайте")
kb.add(but1)
kb.add(but2)
kb.add(but3)


@dp.message_handler(commands=["start"])
async def start_commands(message: types.Message):
    await bot.send_message(message.chat.id, text="привет!", reply_markup=kb)


@dp.message_handler(Text(equals="Все автомобили на сайте"))
async def list_car_bmw(message: types.Message):
    await message.answer("Идет загрузка\nОжидайте...")

    for page_num in range(1, 10):
        time.sleep(2)
        url2 = f"https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=1946&page={page_num}"

        req = requests.get(url2, headers=headers1)
        page = req.text

        soup = BeautifulSoup(page, "lxml")

        cars_list = soup.find_all("div", class_="listing-item")
        for car in cars_list:
            name_car = car.find("a", class_="listing-item__link").text
            car_params_transmission = car.find("div", class_="listing-item__params").find_next().find_next().text
            price_rub = car.find("div", class_="listing-item__prices").find_next().text
            price_usd = car.find("div", class_="listing-item__prices").find_next().find_next().text
            local = car.find("div", class_="listing-item__location").next_element.text
            date_ = car.find("div", class_="listing-item__date").next_element.text
            link_car = "https://cars.av.by" + car.find("a", class_="listing-item__link").get("href")
            list_bmw.append(
                {
                    'название': name_car,
                    'параметры': car_params_transmission,
                    'цена rub': price_rub,
                    'цена usb': price_usd,
                    'место нахождения': local,
                    'дата размещения объявления': date_,
                    'ссылка': link_car,
                })
            time.sleep(0.5)

            with open('dict_list.json', 'w', encoding='UTF-16') as file:
                json.dump(list_bmw, file, indent=4, ensure_ascii=False)

            list_bmw_message = f"{name_car}\n 'параметры': {car_params_transmission},\n" \
                               f"'цена rub': {price_rub},\n'цена usb': {price_usd},\n'место нахождения': {local},\n" \
                               f"'дата размещения объявления': {date_},\n'ссылка': {link_car}"

            await bot.send_message(message.chat.id, list_bmw_message, reply_markup=kb)
    await message.answer("Все объявления высланы.")


@dp.message_handler(Text(equals="Объявления с первой страницы"))
async def list_first_page(message: types.Message):
    req = requests.get(url, headers=headers1)
    page = req.text

    soup = BeautifulSoup(page, "lxml")
    cars_list = soup.find_all("div", class_="listing-item")
    for car in cars_list:
        time.sleep(1)
        name_car = car.find("a", class_="listing-item__link").text
        car_params_transmission = car.find("div", class_="listing-item__params").find_next().find_next().text
        price_rub = car.find("div", class_="listing-item__prices").find_next().text
        price_usd = car.find("div", class_="listing-item__prices").find_next().find_next().text
        local = car.find("div", class_="listing-item__location").next_element.text
        date_ = car.find("div", class_="listing-item__date").next_element.text
        link_car = "https://cars.av.by" + car.find("a", class_="listing-item__link").get("href")

        list_bmw_message = f"{name_car}\n Параметры: {car_params_transmission},\n" \
                           f"Цена rub: {price_rub},\nЦена usb: {price_usd},\nМесто нахождения: {local},\n" \
                           f"Дата размещения объявления: {date_},\nСсылка: {link_car}"

        await bot.send_message(message.chat.id, list_bmw_message, reply_markup=kb)
    await message.answer("Все объявления высланы.")


@dp.message_handler(Text(equals="Всего объявлений на сайте"))
async def list_first_page(message: types.Message):
    with open("dict_list.json", "r", encoding="utf-16") as file:
        cars_list_bmw = json.load(file)

        len_list = len(cars_list_bmw)
        await message.answer(f"Всего объявлений о продаже этой машины - {len_list}")


if __name__ == "__main__":
    print("К работе готов!")
    executor.start_polling(dp)
