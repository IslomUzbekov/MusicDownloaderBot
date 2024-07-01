from aiogram import types


async def start_command(message: types.Message):
    """
    Обработчик команды /start.
    """
    await message.reply("Привет! Отправьте название песни, чтобы скачать её.")


async def help_command(message: types.Message):
    """
    Обработчик команды /help.
    """
    help_text = (
        "Доступные команды:\n"
        "/start - Запуск бота\n"
        "/help - Показать это сообщение\n"
        "/about - Информация о боте\n"
        "Просто отправьте название песни, чтобы скачать её."
    )
    await message.reply(help_text)


async def about_command(message: types.Message):
    """
    Обработчик команды /about.
    """
    about_text = "Этот бот позволяет скачивать музыку по названию из различных сайтов."
    await message.reply(about_text)
