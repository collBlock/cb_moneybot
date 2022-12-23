from openpyxl import load_workbook
from datetime import date, datetime
from count_run import n

today = date.today()

# прописываем кординаты с учетом счетчика
dates_link  = f"A{2+n}"  # ссылка на ячейку с датой
money_link  = f"B{2+n}"  # ссылка на сколько заработал
counts_link = f"C{2+n}"  # сколько заказов
time_link   = f"D{2+n}"  # разница времени работы
start_link  = f"D{3+n}"  # колхоз начало работы
stop_link   = f"D{4+n}"  # колхоз конец  работы
type_link   = f"G{2+n}"  # на чем заработал

wb = load_workbook(filename='way_to_dream.xlsx')
ws = wb['новая сводка']

def dates():  # сохраним дату сегодня
    ws[dates_link] = today  # сохраним в ячейку с датой сегодняшнюю
    wb.save('way_to_dream.xlsx')

def money(int):  # запишем сколько заработали
    ws[money_link] = int  # сохраним в ячейку с датой сегодняшнюю
    wb.save('way_to_dream.xlsx')


def counts(int):  # просим ввести сколько заказов
    ws[counts_link] = int  # сохраним в ячейку с датой сегодняшнюю
    wb.save('way_to_dream.xlsx')

def start():  # записываем время сейчас старт
    now = datetime.now()
    ws[start_link] = now.strftime("%H:%M")
    with open('bot\count_run.py', 'w') as file:  # накидываем на счетчик +1
        file.write(f'n = {n+1}')

    wb.save('way_to_dream.xlsx')


def stop():  # записываем время конца
    now = datetime.now()
    ws[stop_link] = now.strftime("%H:%M")
    #ws[time_link] = f'={stop}-{start}'
    wb.save('way_to_dream.xlsx')



def type(str):  # вводим на чем заработали
    ws[type_link] = str  # сохраним в ячейку с датой сегодняшнюю
    wb.save('way_to_dream.xlsx')