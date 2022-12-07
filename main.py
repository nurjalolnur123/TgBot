import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = '5708808543:AAE7QDlXLn_UYI8uo0tc6IisFyJMqYq0m6M'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    with open('users.txt', 'a') as f:
        f.write('0')

    await message.reply("<b>👋 Salom! Xush kelibsiz. Men sizga ve-saytlarning faviconini yuklab beraman!\n🌐 Veb-saytning ssilkasini jo'natish uchun:</b> /favicon\n<b>🧑‍💻 Dasturchi: </b>@uz_developer_uz @jalol_dev", parse_mode='html')



@dp.message_handler(commands=['favicon'])
async def favicon(message: types.Message):
 
    await message.reply("✅ Veb-saytning ssilkasini domain.com tarzida yuboring!\n❌ https://domain.com tarzida emas!")

    @dp.message_handler()
    async def favicon_in(message: types.Message):
        await message.reply(f"https://icon.horse/icon/{message.text}")

@dp.message_handler(commands=['dasturchi'])
async def favicon(message: types.Message):
 
    await message.reply("<b>😉 Agar muammo bo'lsa @uz_developer_uz @jalol_dev ga murojat qiling</b>", parse_mode='html')

@dp.message_handler(commands=['users'])
async def favicon(message: types.Message):
    users = 0
    with open('users.txt','r') as r:
        read = r.read()

    for s in read:
        users+=1
    await message.reply(f"📊Foydalanuvchilar soni: <i>{users}ta</i>", parse_mode='html')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)