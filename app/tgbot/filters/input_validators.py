from aiogram.filters import BaseFilter
from aiogram.types import Message


class ValidTenderIdInput(BaseFilter):
    async def __call__(self, message: Message):
        lines = message.text.split('\n') 
        if len(lines) > 5:
            await message.reply('Я пока не могу обработать за раз такой объём информации. Введите не больше 5 значений')
            return False
        return True
