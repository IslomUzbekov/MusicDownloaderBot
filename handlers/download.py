import logging
import os

from aiogram import types
from utils.downloader import download_music
from utils.history import save_search_history


async def handle_message(message: types.Message):
    song_name = message.text
    user_id = message.from_user.id
    await message.reply(f"Ищем песню: {song_name}")

    try:
        file_path = download_music(song_name)
        await message.reply("Песня найдена! Скачиваем...")

        with open(file_path, 'rb') as audio_file:
            await message.answer_audio(audio_file)

        os.remove(file_path)
        save_search_history(user_id, song_name)
    except Exception as e:
        await message.reply(f"Ошибка при скачивании: {str(e)}")
        logging.error(f"Ошибка при скачивании: {str(e)}")
