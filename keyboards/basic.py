from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)


def make_start_keyboard():
    start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    start_keyboard.add(KeyboardButton(text="👀 My nodes"))
    return start_keyboard



def add_issue_buttons(issue_id):
    edit_issue_button = InlineKeyboardButton(
        'Restart node', callback_data=f'edit_{issue_id}'
    )
    cancel_issue_button = InlineKeyboardButton(
        'Cancel', callback_data=f'cancel_{issue_id}'
    )
    issue_inline_kb = InlineKeyboardMarkup().add(edit_issue_button)
    issue_inline_kb.add(cancel_issue_button)
    return issue_inline_kb

def add_cancel_button():
    start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    start_keyboard.add(KeyboardButton(text="👀 My nodes"))
    return start_keyboard

