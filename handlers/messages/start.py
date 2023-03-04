from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from keyboards.basic import make_start_keyboard
from text_messages import Messages


async def start(m: Message, state: FSMContext):
    """
    Responds to /start with basic greeting
    """
    await m.answer(
        f"{Messages.START.value}", reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )
    
