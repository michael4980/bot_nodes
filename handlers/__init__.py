import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Regexp, RegexpCommandsFilter, Text

import handlers.callbacks.issues as issues_callbacks

import handlers.messages.issues as issues
import handlers.messages.text_test as text



from handlers.messages.start import start
from handlers.messages.unknown import unknown


def setup(dp: Dispatcher):
    """
    Setup handlers
    """
    # order details by number (regexp)
    dp.register_message_handler(
        issues.node_details,
        Regexp("node[0-9]+")
    )
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
    dp.register_callback_query_handler(
        issues_callbacks.start_node,
        Regexp('start_node[0-9]+'),
        state='*'
    )
    
    dp.register_callback_query_handler(
        issues_callbacks.stop_node,
        Regexp('stop_node[0-9]+'),
        state='*'
    )
     
    dp.register_callback_query_handler(
        issues_callbacks.cancel_process,
        Regexp('cancel_process_node[0-9]+'),
        state='*'
    )
    
    logging.info('setup done')
