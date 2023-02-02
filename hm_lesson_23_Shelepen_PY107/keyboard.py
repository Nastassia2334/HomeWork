from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

inline_kb = InlineKeyboardMarkup()
inline_kb_info = InlineKeyboardButton(text="Информация о Python",
                                      url='https://ru.wikipedia.org/wiki/Python')
inline_kb_list = InlineKeyboardButton(text="Cписок полезной литературы",
                                      url='https://zavistnik.com/7-luchshih-knig-po-python/')
inline_kb.add(inline_kb_info, inline_kb_list)

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb1 = KeyboardButton("Зима")
start_kb2 = KeyboardButton("Весна")
start_kb3 = KeyboardButton("Осень")
start_kb4 = KeyboardButton("Лето")
start_kb.add(start_kb1, start_kb2)
start_kb.add(start_kb3, start_kb4)

kb_time = InlineKeyboardMarkup()
kb_time.add(InlineKeyboardButton("Да", callback_data="like"))
kb_time.add(InlineKeyboardButton("Нет", callback_data="no"))







