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


s = {}


bot = Bot(token="2071229081:AAFEs-aotdzKVpyKP3elnmpO2BP3npfiGQs")
dp = Dispatcher(bot, storage=MemoryStorage())







@dp.message_handler(commands=['test'], state = None)
async def test(msg: types.Message):
    await msg.answer("1?")
    await stt.Q1.set()


@dp.message_handler(state = stt.Q1)
async def ans1(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(answer1 = answer)
    await msg.answer("2?")
    await stt.next()

@dp.message_handler(state = stt.Q2)
async def ans2(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = msg.text
    await state.finish()

@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Начнём", callback_data="Menu"))
    await msg.answer("Начнём?", reply_markup=keyboard)



@dp.callback_query_handler(text="Menu")
async def menu(msg : types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Добавить игру", callback_data="addGame"))
    keyboard.add(types.InlineKeyboardButton(text="Текущие настройки", callback_data="status"))







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