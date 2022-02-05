from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import gamePriceParser as sp
import asyncio
import datetime


s = {}


bot = Bot(token="2071229081:AAFEs-aotdzKVpyKP3elnmpO2BP3npfiGQs")
dp = Dispatcher(bot)







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


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, sp.gamePrice(msg.text))

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