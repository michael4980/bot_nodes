import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Regexp, RegexpCommandsFilter, Text

import handlers.callbacks.issues as issues_callbacks

import handlers.messages.issues as issues
from handlers.callbacks.issues import cancel_issue


from handlers.messages.start import start
from handlers.messages.unknown import unknown


def setup(dp: Dispatcher):
    """
    Setup handlers
    """
    # to cancel anything
    dp.register_message_handler(
        cancel_issue,
        Text(equals='🙅 Отмена', ignore_case=True),
        state='*'
    )
    

    # order details by number (regexp)
    # dp.register_message_handler(
    #     issues.issue_details,
    #     RegexpCommandsFilter(regexp_commands=['\\d+'])
    # )
    # # single messages
    dp.register_message_handler(start, commands=["start"])
    
    
    # view all my orders
    dp.register_message_handler(
        issues.my_nodes, Text(equals='👀 My nodes', ignore_case=True),
        state='*'
    )
  
    # HAS TO BE THE LAST MESSAGE HANDLER
    dp.register_message_handler(
        unknown, state='*'
    )

    # callbacks
    # dp.register_callback_query_handler(
    #     answer_to_lement,
    #     Regexp('answer_lement_\\d+'),
    #     state='*'
    # )
    # rate issue
    # dp.register_callback_query_handler(
    #     issues_callbacks.rate_issue,
    #     Regexp('rate_issue_.+'),
    #     state='*'
    # )
    logging.info('setup done')
