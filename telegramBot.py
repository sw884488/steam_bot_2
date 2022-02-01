from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import gamePriceParser as sp





bot = Bot(token="2071229081:AAFEs-aotdzKVpyKP3elnmpO2BP3npfiGQs")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("test")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    await bot.send_message(msg.from_user.id, sp.gamePrice(msg.text))


if __name__ == '__main__':
    executor.start_polling(dp)