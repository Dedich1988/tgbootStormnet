from telebot.types import ReplyKeyboardMarkup, KeyboardButton


check_button = ReplyKeyboardMarkup(resize_keyboard=True)
item1 = KeyboardButton("Проверить")
check_button.add(item1)