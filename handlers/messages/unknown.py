from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def unknown(m: Message, state: FSMContext):
    await state.finish()
    """
    Responds to unknown messages
    """
    await m.answer(
        "Wrong input\
        /start"
    )
