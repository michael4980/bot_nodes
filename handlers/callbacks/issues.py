import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
# from keyboards.basic import (add_cancel_button, add_edit_buttons,
#                              leave_comment_keyboard, make_start_keyboard)
from text_messages import Messages


async def cancel_issue(query: types.CallbackQuery):
    await query.message.answer('Отменяю заявку...')
    await query.answer()  # to remove clock sign at button
    await query.message.answer('Заявка отменена!')


