import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
import sqlite3
import keyboards
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State
connection = sqlite3.connect('DataBase.db')
cursor = connection.cursor()


logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6761875897:AAH64MP4_DERouKQrOPeIShCJYNhHxPbTX8", parse_mode="HTML")
# Диспетчер
dp = Dispatcher()
class priem(StatesGroup):
    tg_id=State()
    doc_id=State()
    date=State()
    time=State()
# Хэндлер на команду /start

@dp.message(Command("start"))
async def start(message:Message, state:FSMContext):
    await state.set_state(priem.tg_id)
    await message.answer(f"Привет, {message.from_user.first_name}! Я бот, который создан для записи в больницу! Выбери нужное ниже ...",reply_markup=keyboards.main_kb)
@dp.message(F.text=="Записаться на приём")
async def priem_name(message:Message,state:FSMContext):
    await state.update_data(tg_id=message.from_user.id)
    await state.set_state(priem.doc_id)
    await message.answer("Выберите специализацию врача", reply_markup=keyboards.docs())

@dp.message(F.text=="Посмотреть записи")
async def about_priem(message:Message,state:FSMContext):
    cursor.execute('SELECT Пациент, Врач, Дата, Время FROM Прием WHERE Пациент = ?',(str(message.from_user.id),))
    items=cursor.fetchall()
    text='Ваши записи: \n\n'
    for item in items:
        text+=f'Врач: {cursor.execute('SELECT id, Фамилия FROM Врачи WHERE id =?',(item[1],)).fetchone()[1]}\n'
        text += f'Дата: {item[2]}\n'
        text += f'Время: {item[3]}\n'
        text+='\n\n'

    await message.answer(text)
@dp.callback_query(keyboards.doctors.filter())
async def doctors_handlers(call: CallbackQuery, callback_data:keyboards.doctors):
    if callback_data.action=="therapist":
        await call.message.edit_text(
            f"Выберите врача из списка", reply_markup=keyboards.doc_ters()
        )
    elif callback_data.action=="surgeon":
        await call.message.edit_text(
            "Выберите врача из списка",reply_markup=keyboards.doc_surgs()
        )
    elif callback_data.action=="ophthalmologist":
        await call.message.edit_text(
            "Выберите врача из списка",reply_markup=keyboards.doc_ophtals()
        )
    elif callback_data.action=="endocrinologist":
        await call.message.edit_text(
            "Выберите врача из списка",reply_markup=keyboards.doc_endos()
        )
    elif callback_data.action=="nevrologist":
        await call.message.edit_text(
            "Выберите врача из списка",reply_markup=keyboards.doc_nevros()
        )
    elif callback_data.action=="psycho":
        await call.message.edit_text(
            "Выберите врача из списка",reply_markup=keyboards.doc_psychos()
        )
@dp.callback_query(keyboards.therapists.filter())
async def terapevts_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    for i in range(25):
        if callback_data.id==i:
            await state.update_data(doc_id = i)
            await state.set_state(priem.date)
            await call.message.edit_text("Выберите дату", reply_markup=keyboards.doc_date())

@dp.callback_query(keyboards.surgeons.filter())
async def terapevts_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    for i in range(25):
        if callback_data.id==i:
            await state.update_data(doc_id = i)
            await state.set_state(priem.date)
            await call.message.edit_text("Выберите дату", reply_markup=keyboards.doc_date())

@dp.callback_query(keyboards.ophthalmologists.filter())
async def terapevts_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    for i in range(25):
        if callback_data.id==i:
            await state.update_data(doc_id = i)
            await state.set_state(priem.date)
            await call.message.edit_text("Выберите дату", reply_markup=keyboards.doc_date())

@dp.callback_query(keyboards.endocrinologists.filter())
async def terapevts_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    for i in range(25):
        if callback_data.id==i:
            await state.update_data(doc_id = i)
            await state.set_state(priem.date)
            await call.message.edit_text("Выберите дату", reply_markup=keyboards.doc_date())

@dp.callback_query(keyboards.nevrologists.filter())
async def terapevts_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    for i in range(25):
        if callback_data.id==i:
            await state.update_data(doc_id = i)
            await state.set_state(priem.date)
            await call.message.edit_text("Выберите дату", reply_markup=keyboards.doc_date())

@dp.callback_query(keyboards.psychos.filter())
async def terapevts_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    for i in range(25):
        if callback_data.id==i:
            await state.update_data(doc_id = i)
            await state.set_state(priem.date)
            await call.message.edit_text("Выберите дату", reply_markup=keyboards.doc_date())

@dp.callback_query(keyboards.date.filter())
async def date_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    items = ['27.05', '28.05', '29.05', '30.05', '31.05', '3.06']
    for i in items:
        if callback_data.str_date==i:
            await state.update_data(date=i)
            await state.set_state(priem.time)
            await call.message.edit_text("Выберите время", reply_markup=keyboards.doc_time())
@dp.callback_query(keyboards.time.filter())
async def time_handlers(call:CallbackQuery,callback_data:keyboards.therapists, state:FSMContext):
    items = ['9.00', '9.30', '10.00', '10.30', '11.00', '11.30', '12.00']
    for i in items:
        if callback_data.str_time==i:
            await state.update_data(time=i)

            data= await state.get_data()
            cursor.execute('SELECT id, Фамилия FROM Врачи WHERE id = ? ',(int(data['doc_id']),))
            res=cursor.fetchall()
            await call.message.edit_text(f"Успешно!\n Ваша запись:\n\n Врач:{res[0][1]}\n\n Дата: {data["date"]}\n\n Время: {data["time"]}")
            patient=data['tg_id']
            doctor=int(data['doc_id'])
            date_priem=data['date']
            time_priem=data['time']
            cursor.execute(
                "INSERT INTO Прием (Пациент, Врач, Дата, Время) VALUES (?, ?, ?, ?)",(patient,doctor,date_priem,time_priem)
            )
            connection.commit()
            await state.clear()

@dp.message()
async def echo(message: Message):
    msg=message.text.lower()



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)