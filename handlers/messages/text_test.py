from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards.basic import make_start_keyboard


async def text_tester(m: Message, state: FSMContext):
    await state.finish()
    await m.answer(
        'Please wait, picking up data...',
        reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )
    await m.answer(
            m.text,
            reply_markup=make_start_keyboard(),
            parse_mode='Markdown'
        )