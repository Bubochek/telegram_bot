import datetime
from datetime import date
import json
import os
import workWithTime


def create_json(id):
    if f'{str(id)}.json' not in os.listdir("data"):
        #Создаём json файл с фигурными скобками внутри
        json.dump({}, open(f'data/{str(id)}.json', 'w'))


#Записываем данные в json файл
#Принимаем значения id пользователя и данные в формате {'sec': секунды тренировки, 'jim': повторения}
def json_Read(id, value):

    #Сегодняшняя дата
    today = date.today().strftime("%d.%m")

    create_json(id)

    #Читаем json файл и переводим в словарь:
    with open(f"data/{str(id)}.json", 'r') as file:
        data = json.load(file)

    # Значение, которые нужно записать (Номер тренировки: {Дата: .., Секунды: .., Жим: ..}):
        data[str(len(data)+1)] = {"date": today, "sec": value['sec'], "jim":value['jim']}

    #Переводим полученные секунды в формат ЧАСЫ:МИНУТЫ:СЕКУНДЫ
        data[str(len(data))]["sec"] = workWithTime.convert_seconds(value['sec'])


    #Словарь переводим в json файл:
    with open(f"data/{str(id)}.json", 'w') as file:
        json.dump(data, file, indent=4)


def get_json_inf(id):
    with open(f'data/{id}.json', 'r') as file:
        data = json.load(file)
        get_result = ''
        for i in range(1,len(data)+1):
            applies = f'Номер тренировки: {i}'
            result = (f'Дата тренировки: {data[str(i)]["date"]}\n'
                      f'Время тренировки: {data[str(i)]["sec"]}\n'
                      f'Кол-во повторений: {data[str(i)]["jim"]}')
            if i == 1:
                get_result += f'{applies}\n{result}'
            else:
                get_result += f'\n\n{applies}\n{result}'
        return get_result

