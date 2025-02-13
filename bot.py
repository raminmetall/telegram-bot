import logging
import asyncio
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "7687737572:AAGhchzRPEbsBKrotnrpFZbtCPwRvhkU4FU"
ADMIN_ID = 6586406054  # آی‌دی ادمین

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # نیازی نیست bot اینجا مقداردهی بشه
logging.basicConfig(level=logging.INFO)

# ذخیره کاربران
users = {}

def calculate_bonus(join_date):
    years_active = datetime.datetime.now().year - join_date.year
    return years_active * 10  # هر سال 10 امتیاز

@dp.message(Command("start"))
async def start(msg: types.Message):
    user_id = msg.from_user.id
    if user_id not in users:
        join_date = datetime.datetime.now()
        users[user_id] = {'points': calculate_bonus(join_date), 'invites': 0}
    
    invite_link = f"https://t.me/YOUR_BOT_USERNAME?start={user_id}"
    await msg.answer(f"سلام {msg.from_user.first_name}!\n\nامتیاز شما: {users[user_id]['points']}\nلینک دعوت شما: {invite_link}")

@dp.message(Command("invite"))
async def invite(msg: types.Message):
    user_id = msg.from_user.id
    invite_link = f"https://t.me/YOUR_BOT_USERNAME?start={user_id}"
    await msg.answer(f"لینک دعوت شما: {invite_link}")

@dp.message(Command("tasks"))
async def tasks(msg: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔗 بازدید لینک", url="https://example.com")],
        [InlineKeyboardButton(text="📢 عضویت در کانال", url="https://t.me/YOUR_CHANNEL")]
    ])
    await msg.answer("✅ تسک‌های روزانه:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)  # اینجا bot رو اضافه کردم

if __name__ == "__main__":
    asyncio.run(main())
