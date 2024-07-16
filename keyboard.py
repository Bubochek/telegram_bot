from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton('Начать тренировку'),
                 KeyboardButton('Мои результаты'))

    return keyboard

def end_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Закончить тренировку'))

    return keyboard

def set_of_exercises():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton('Жим'),
                 KeyboardButton('Подтягивания'),
                 KeyboardButton('Начать тренировку'))

    return keyboard