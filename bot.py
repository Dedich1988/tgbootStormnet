import os
import telebot
import sqlite3

from hh_parsing import parse_data
from handle_data import handel_vacancies
from keyboards import check_button

token = '1883789591:AAFZdm3Sclaf1WeksXlk5IczZdTCxO5BSHc'
bot = telebot.TeleBot(token)

conn = sqlite3.connect('../botbd.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(chat_id: str, note: str):
	cursor.execute('INSERT INTO hh_vacation (chat_id, note) VALUES (?, ?)', (chat_id, note))
	conn.commit()

@bot.message_handler(commands=['start'])
def strat_bot(message):
    bot.send_message(message.chat.id, 'Бот готов к поиску вакансий', reply_markup=check_button)


@bot.message_handler(regexp='Проверить')
def get_vacancy(message):
    raw_data = parse_data()
    data = handel_vacancies(raw_data)
    if not data:
        bot.send_message(message.chat.id, 'новых вакансий нет..')
    else:
        for text in data:
            bot.send_message(message.chat.id, text, parse_mode='html')
            db_table_val(message.chat.id, text)



@bot.message_handler()
def another_answer(message):
    bot.send_message(message.chat.id, 'Не понимаю.. Нажмите кнопку Проверить!', reply_markup=check_button)


if __name__ == '__main__':
     bot.infinity_polling()