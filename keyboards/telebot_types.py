from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def answer_to_lement(issue_id):
    answer_keyboard = InlineKeyboardMarkup()
    answer_keyboard.add(
        InlineKeyboardButton(
            f'Ответить',
            callback_data=f'answer_lement_{issue_id}'
        )
    )
    return answer_keyboard

'''inline buttons add 6 button'''
def rate_issue(issue_id):
    rate_keyboard = InlineKeyboardMarkup()
    buttons = []
    for i in range(1, 6):
        buttons.append(
            InlineKeyboardButton(
                f'{i}',
                callback_data=f'rate_issue_{issue_id}_{i}'
            )
        )
    buttons.append(InlineKeyboardButton('Доработать', callback_data=f'rate_issue_{issue_id}_{6}'))
    rate_keyboard.add(*buttons)
    return rate_keyboard
