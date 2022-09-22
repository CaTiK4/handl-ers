# Import library
from app import bot, do
from aiogram import types
from aiogram.types import Message

keyboard_markup = types.ReplKeyboardMarkup(row_width=3)

# Array for keyboard
array_keyboard = [1, 2]

# Send messageg to admin
async def send_to_admin(do):
    await bot.send_message(chat_id=155752773, text="bot start")

# Function of start bot
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.keyboardButton(texty) fro text in array_keyboard)
    await message.answer(text='Hello!', reply_markup=keyboard_markup)
