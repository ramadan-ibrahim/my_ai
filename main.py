import os
import openai
import asyncio
from aiogram import Bot, Dispatcher, types

# جلب القيم من بيئة GitHub Actions
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message_handler()
async def chat_with_ai(message: types.Message):
    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": message.text}],
        api_key=DEEPSEEK_API_KEY
    )
    await message.reply(response["choices"][0]["message"]["content"])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 
