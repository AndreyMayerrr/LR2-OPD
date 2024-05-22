from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
import sqlite3

connection = sqlite3.connect('DataBase.db')
cursor = connection.cursor()

main_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Записаться на приём"),
            KeyboardButton(text="Посмотреть записи")
        ]
    ],resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder= "Выберите действие из меню"
)



class doctors (CallbackData, prefix="doc"):
    action: str

def docs():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Терапевт", callback_data=doctors(action="therapist").pack()),
        InlineKeyboardButton(text="Хирург", callback_data=doctors(action="surgeon").pack()),
        InlineKeyboardButton(text="Офтальмолог", callback_data=doctors(action="ophthalmologist").pack()),
        InlineKeyboardButton(text="Эндокринолог", callback_data=doctors(action="endocrinologist").pack()),
        InlineKeyboardButton(text="Невролог", callback_data=doctors(action="nevrologist").pack()),
        InlineKeyboardButton(text="Психиатр", callback_data=doctors(action="psycho").pack()),
        width=2

    )
    return builder.as_markup()
class therapists (CallbackData, prefix="ter"):
    id: int

def doc_ters():
    cursor.execute('SELECT id,Фамилия, Имя, Отчество FROM Врачи WHERE Специальность = ?', ('Терапевт',))
    results = cursor.fetchall()
    builder = InlineKeyboardBuilder()
    for data in results:
        builder.row(
            InlineKeyboardButton(text=f"{data[1]} {data[2]} {data[3]}", callback_data=therapists(id=data[0]).pack()),
        width=1
    )
    return builder.as_markup()

class surgeons (CallbackData, prefix="surg"):
    id: int

def doc_surgs():
    cursor.execute('SELECT id,Фамилия, Имя, Отчество FROM Врачи WHERE Специальность = ?', ('Хирург',))
    results = cursor.fetchall()
    builder = InlineKeyboardBuilder()
    for data in results:
        builder.row(
            InlineKeyboardButton(text=f"{data[1]} {data[2]} {data[3]}", callback_data=therapists(id=data[0]).pack()),
            width=1
        )
    return builder.as_markup()

class ophthalmologists (CallbackData, prefix="ophtals"):
    id: int

def doc_ophtals():
    cursor.execute('SELECT id,Фамилия, Имя, Отчество FROM Врачи WHERE Специальность = ?', ('Офтальмолог',))
    results = cursor.fetchall()
    builder = InlineKeyboardBuilder()
    for data in results:
        builder.row(
            InlineKeyboardButton(text=f"{data[1]} {data[2]} {data[3]}", callback_data=ophthalmologists(id=data[0]).pack()),
            width=1
        )
    return builder.as_markup()

class endocrinologists (CallbackData, prefix="endos"):
    id: int

def doc_endos():
    cursor.execute('SELECT id,Фамилия, Имя, Отчество FROM Врачи WHERE Специальность = ?', ('Эндокринолог',))
    results = cursor.fetchall()
    builder = InlineKeyboardBuilder()
    for data in results:
        builder.row(
            InlineKeyboardButton(text=f"{data[1]} {data[2]} {data[3]}",
                                 callback_data=endocrinologists(id=data[0]).pack()),
            width=1
        )
    return builder.as_markup()

class nevrologists (CallbackData, prefix="nevros"):
    id: int

def doc_nevros():
    cursor.execute('SELECT id,Фамилия, Имя, Отчество FROM Врачи WHERE Специальность = ?', ('Невролог',))
    results = cursor.fetchall()
    builder = InlineKeyboardBuilder()
    for data in results:
        builder.row(
            InlineKeyboardButton(text=f"{data[1]} {data[2]} {data[3]}",
                                 callback_data=nevrologists(id=data[0]).pack()),
            width=1
        )
    return builder.as_markup()

class psychos (CallbackData, prefix="psychos"):
    id: int

def doc_psychos():
    cursor.execute('SELECT id,Фамилия, Имя, Отчество FROM Врачи WHERE Специальность = ?', ('Психиатр',))
    results = cursor.fetchall()
    builder = InlineKeyboardBuilder()
    for data in results:
        builder.row(
            InlineKeyboardButton(text=f"{data[1]} {data[2]} {data[3]}",
                                 callback_data=psychos(id=data[0]).pack()),
            width=1
        )
    return builder.as_markup()

class time(CallbackData, prefix='tm'):
    str_time: str

def doc_time():
    items=['9.00','9.30','10.00','10.30','11.00','11.30','12.00']
    builder = InlineKeyboardBuilder()
    for item in items:
        builder.button(text=item,callback_data=time(str_time=item))
    return builder.as_markup()

class date(CallbackData, prefix='dt'):
    str_date: str

def doc_date():
    items = ['27.05', '28.05', '29.05', '30.05', '31.05', '3.06']
    builder = InlineKeyboardBuilder()
    for item in items:
        builder.button(text=item, callback_data=date(str_date=item))
    return builder.as_markup()