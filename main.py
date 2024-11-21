import os
import asyncio
from bs4 import BeautifulSoup
import random
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


url = 'https://www.anekdot.ru/random/anekdot/'
TOKEN = os.getenv('TOKEN')






async def anekdot(message: types.Message):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    anekdot = soup.find('div', class_="text")
    joke = anekdot.get_text(separator='\n')
    await message.answer(joke)



async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.message.register(anekdot, Command(commands='anekdot'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print('Exit')