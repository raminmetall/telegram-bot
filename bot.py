import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# 🛑 حتماً توکن خود را جایگزین کن!
TOKEN = "7687737572:AAGhchzRPEbsBKrotnrpFZbtCPwRvhkU4FU"
ADMIN_ID = 6586406054  # آی‌دی عددی ادمین

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# 🔹 لینک هاست مینی‌اپلیکیشن (مثلاً روی Render یا Vercel)
WEB_APP_URL = "https://index-7e6z.onrender.com"

# 🖥️ ایجاد کیبورد با دکمه WebApp
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚀 باز کردن مینی‌اپ", web_app=WebAppInfo(url=WEB_APP_URL))]
    ],
    resize_keyboard=True
)

@dp.message(lambda message: message.text == "/start")
async def start(msg: types.Message):
    await msg.answer("سلام! برای اجرای مینی‌اپ، روی دکمه زیر کلیک کن:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "/miniapp")
async def send_miniapp(message: types.Message):
    await message.answer("روی دکمه زیر کلیک کن تا مینی‌اپ باز بشه:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
