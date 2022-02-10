from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import gamePriceParser as sp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
import datetime
from states import test as stt
import gameSearchParser as gsp
import gameSearchAnswer as gsa


bot = Bot(token="2071229081:AAFEs-aotdzKVpyKP3elnmpO2BP3npfiGQs")
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(
        "Привет! Это бот для мониторинга цен на игры в Steam. Чтобы начать, напишите /s или выберите 'Начать' в меню")




if __name__ == '__main__':
    executor.start_polling(dp)