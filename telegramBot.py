from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import gamePriceParser as sp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
import datetime
from  states import test  as stt
import gameSearchParser as gsp
import gameSearchAnswer as gsa



user_data = {}
games_list = {}


bot = Bot(token="2071229081:AAFEs-aotdzKVpyKP3elnmpO2BP3npfiGQs")
dp = Dispatcher(bot, storage=MemoryStorage())




@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("Привет! Это бот для мониторинга цен на игры в Steam. Чтобы начать, напишите /s или выберите 'Начать' в меню")
    user_data[msg.from_user.id] = []


@dp.message_handler(commands=['help'], state="*")
async def start(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer("Это бот для мониторинга цен на игры в Steam. Чтобы начать, напишите /s или выберите 'Добавить игру в меню' в меню")


@dp.message_handler(commands=['s'], state = None)
async def test(msg: types.Message):
    await msg.answer("Напишите название игры")
    await stt.waiting_for_game_name.set()


@dp.message_handler(commands=['cancel'], state="*")
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено. Для старта напишите /s ")


@dp.message_handler(state = stt.waiting_for_game_name)
async def ans1(msg: types.Message, state: FSMContext):
    answer = msg.text
    l = gsp.gameSearch(msg.text)
    print(l)
    q = 0
    for key, value in l.items():
        await msg.answer(str(q) + ". " + str(key) + ". " + value)
        games_list[q] = l[key]
        q += 1
    await state.update_data(answer1 = answer)
    await msg.answer("Напишите номер игры. Если игры нет в списке, повторите поиск, уточнив название")
    await stt.next()


@dp.message_handler(state = stt.waiting_for_game_number)
async def ans2(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = msg.text
    user_data[msg.from_user.id].append(games_list[int(msg.text)])
    await msg.answer("Данные получены")
    await state.finish()




@dp.message_handler()
async def f(msg: types.message):
    await msg.answer(user_data[msg.from_user.id])
    print(user_data)

















# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("test")
#     asyncio.create_task(scheduler(datetime.datetime(2022, 2, 3, 11, 7)))


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, sp.gamePrice(msg.text))

async def testf(n):
    await bot.send_message(n, "msg.text")


async def scheduler(dt):
    now = datetime.datetime.now()
    await asyncio.sleep((dt - now).total_seconds())
    print(1)




async def on_startup(_):
    asyncio.create_task(scheduler(datetime.datetime(2022, 2, 3, 11, 5)))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)