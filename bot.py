import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config.bot_config import BOT_TOKEN
from handlers.download import handle_message
from handlers.handlers import about_command, help_command, start_command

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Регистрация обработчиков команд
dp.message.register(start_command, Command('start'))
dp.message.register(help_command, Command('help'))
dp.message.register(about_command, Command('about'))
dp.message.register(handle_message)


# Основная функция для запуска бота
async def main():
    logging.info("Starting bot...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
