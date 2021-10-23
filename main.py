from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from itranslate import itranslate as tarjima

bot = Bot(token='2066336127:AAGv0PKfHGDekqTeIFNLxDIwrD0ZG1sGhgE', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(Text(equals=["start", "/start"]))
async def get_start(message: types.Message):
   await message.answer(text='Botdan foydalanishingiz mumkin 😉. So`z kiriting inglizchaga tarjima qiladi ✅!')

@dp.message_handler(Text(equals=["dasturchi", "/devoloper", "devoloper"]))
async def get_start(message: types.Message):
   await message.answer(text='👨‍💻 @Devoloper1')


@dp.message_handler()
async def get_message(message: types.Message):
    await message.reply(text=f'Siz kiritgan so`z: <b>{message.text}</b>'+'\nTarjimasi: '+'<b>'+tarjima(message.text,to_lang='en')+'</b>')

executor.start_polling(dp)