from aiogram import Bot
import asyncio


async def send_message_bot(text,
                     chat_id='your_chat_id',
                     token='your_token'):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=text)
    await bot.session.close()

#h
