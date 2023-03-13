from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)


def make_start_keyboard():
    start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    start_keyboard.add(KeyboardButton(text="👀 My nodes"))
    return start_keyboard



def start_node_button(node_num):
    start_button = InlineKeyboardButton(
        'Start node', callback_data=f'start_{node_num}'
    )
    cancel_button = InlineKeyboardButton(
        '🙅 Cancel', callback_data=f'cancel_process_{node_num}'
    )
    node_inline = InlineKeyboardMarkup().add(start_button)
    node_inline.add(cancel_button)
    return node_inline

def stop_node_button(node_num):
    stop_button = InlineKeyboardButton(
        'Stop node', callback_data=f'stop_{node_num}'
    )
    cancel_button = InlineKeyboardButton(
        '🙅 Cancel', callback_data=f'cancel_process_{node_num}'
    )
    node_inline = InlineKeyboardMarkup().add(stop_button)
    node_inline.add(cancel_button)
    return node_inline

def add_cancel_button():
    start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    start_keyboard.add(KeyboardButton(text="👀 My nodes"))
    return start_keyboard

