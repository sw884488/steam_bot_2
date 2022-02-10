from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import gamePriceParser as sp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
import gameSearchParser as gsp
import gameSearchAnswer as gsa




bot = Bot(token="2071229081:AAFEs-aotdzKVpyKP3elnmpO2BP3npfiGQs")
dp = Dispatcher(bot, storage=MemoryStorage())


games_list = {}
user_data = {}




@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(
        "Привет! Это бот для мониторинга цен на игры в Steam. Чтобы начать, напишите /s или выберите 'Добавить игру' в меню")


@dp.message_handler(commands=['cancel'], state="*")
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено. Для старта напишите /s ")


@dp.message_handler(commands=['help'], state="*")
async def start(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(
        "Это бот для мониторинга цен на игры в Steam. Чтобы начать, напишите /s или выберите 'Добавить игру в меню' в меню")


async def scheduler(msg: types.Message, n):
    await msg.answer(sp.gamePrice(n))




@dp.message_handler(commands=['s'])
async def s(msg: types.Message, state: FSMContext):
    await msg.answer("Напишите название игры")
    await state.set_state('waiting_for_game_name')


@dp.message_handler(state='waiting_for_game_name')
async def gameName(msg: types.Message, state: FSMContext):
    await state.set_state('waiting_for_game_number')
    l = gsp.gameSearch(msg.text)
    q = 1
    if len(l) > 0:
        for key, value in l.items():
            await msg.answer(str(q) + ". " + str(key) + "\n")

            await asyncio.sleep(0.5)
            games_list[q] = l[key]
            q += 1
        await msg.answer("Выберите номер игры из списка")
    else:
        await msg.answer("Ничего не найдено. Попробуйте изменить запрос и выполните поиск заново. Для этого напишите /s или выберите 'Добавить игру' в меню")
        await state.finish()


@dp.message_handler(state='waiting_for_game_number')
async def gameNumber(msg: types.Message, state: FSMContext):
    user_data[msg.from_user.id] = ""
    if msg.text.isnumeric() == False or int(msg.text) > len(games_list) or int(msg.text) == 0:
        await msg.answer("Вы ввели не число или число вне диапазона")
    else:
        await state.finish()
        user_data[msg.from_user.id] = games_list[int(msg.text)]
        await asyncio.create_task(scheduler(msg, user_data[msg.from_user.id]))




if __name__ == '__main__':
    executor.start_polling(dp)