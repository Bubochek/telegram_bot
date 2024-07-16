import telebot
from telebot import types
import keyboard
import jsonRead
import workWithTime

bot = telebot.TeleBot('7093821193:AAHq_CCVusOYaV8DhezugvB511nLaF5GQjM')

result = {}
status_code = []

@bot.message_handler(commands=['start'])

def hi(message):
    bot.send_message(message.chat.id, 'Это тренБот', reply_markup=keyboard.get_keyboard())


@bot.message_handler(content_types=['text'])

def tren(message):


    #Начало тренировки
    if message.text.lower() == 'начать тренировку':
        bot.send_message(message.chat.id, 'Тренировка началась, запиши количество повторений', reply_markup=keyboard.end_keyboard())
        result[message.chat.id] = {"sec": workWithTime.find_time(), "jim": 0}
        status_code.append(message.chat.id)


    #Конец тренировки
    elif message.text.lower() == 'закончить тренировку':
        bot.send_message(message.chat.id, 'Твои результаты записаны', reply_markup=keyboard.get_keyboard())

        #Завершаем тренировку и записываем в словарь по формуле: (конец тренировки) - (начало тренировки) = время тренировки
        result[message.chat.id] = {"sec": workWithTime.find_time() - result[message.chat.id]['sec'], "jim": int(result[message.chat.id]["jim"])}

        #Отправляем в jsonRead в формате {'sec': время, 'jim': повторения}
        jsonRead.json_Read(message.chat.id, result[message.chat.id])

        #Удаляем информацию из словаря и статус кода
        del result[message.chat.id]
        status_code.remove(message.chat.id)


    #Запись результатов
    else:
        if message.chat.id in status_code:
            try:
                int(message.text)
                bot.send_message(message.chat.id, 'Результат записан', reply_markup=keyboard.end_keyboard())
                result[message.chat.id]["jim"] = message.text
            except ValueError:
                bot.send_message(message.chat.id, 'Отправь целое число')


    if message.text.lower() == 'мои результаты':
        bot.send_message(message.chat.id, f"Все твои тренировки:\n\n{jsonRead.get_json_inf(message.chat.id)}")

bot.infinity_polling()