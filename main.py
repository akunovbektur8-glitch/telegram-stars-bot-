import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "9193338763:AAEtYHREzkWmwfMDlNFrBrYUTwjaDY-D2cs"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Купить звезды")],
        [KeyboardButton(text="📢 Наш канал"), KeyboardButton(text="💬 Наш чат")],
        [KeyboardButton(text="⭐ Отзывы")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Приветствую тебя в боте по покупке Telegram Stars! ⭐️\n"
        "Выберите нужный раздел в меню ниже:",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "🛒 Купить звезды")
async def process_buy_stars(message: types.Message):
    price_text = (
        "🌟 Прайс на звёзды Telegram:\n\n"
        "⭐️ 50 — 120 сом | 140 ₽ 💰\n"
        "⭐️ 100 — 2$ — 175 сом | 160 ₽ 💰\n"
        "⭐️ 250 — 5$ — 437 сом | 425 ₽ 💰\n"
        "⭐️ 350 — 7$ — 612 сом | 600 ₽ 💰\n"
        "⭐️ 500 — 10$ — 875 сом | 850 ₽ 💰\n"
        "⭐️ 750 — 15$ — 1312 сом | 1300 ₽ 💰\n"
        "⭐️ 1000 — 20$ — 1650 сом | 1600 ₽ 💰\n\n"
        "💳 Оплата по QR-коду выше.\n"
        "📌 После оплаты обязательно отправьте чек администратору: @norkinsss"
    )
    try:
        photo = FSInputFile("qr.jpg")
        await message.answer_photo(photo=photo, caption=price_text)
    except Exception:
        await message.answer(price_text)

@dp.message(F.text == "📢 Наш канал")
async def process_channel(message: types.Message):
    await message.answer("📢 Наш официальный канал: https://t.me/norkinssstars")

@dp.message(F.text == "💬 Наш чат")
async def process_chat(message: types.Message):
    await message.answer("💬 Наш уютный чат для общения: https://t.me/chatnorkinssss")

@dp.message(F.text == "⭐ Отзывы")
async def process_reviews(message: types.Message):
    await message.answer("⭐ Почитать отзывы наших клиентов можно здесь: https://t.me/norkinssotziv")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
