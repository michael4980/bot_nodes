import logging
from aiogram import types
from configparser import ConfigParser
from keyboards.basic import add_cancel_button
from handlers.messages.utils import Node
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

async def cancel_process(query: types.CallbackQuery):
    await query.message.answer('Cancel picking info')
    await query.answer()  # to remove clock sign at button
    await query.message.answer('Back to node list')

async def start_node(query: types.CallbackQuery):
    
    await query.answer()  # to remove clock sign at button
    await query.message.answer(
        'Trying to restart node...',
        reply_markup=add_cancel_button(),
        parse_mode='Markdown'
    )
    num = query.data.split('_')[1]
    host = config.get(num, 'ip')
    pas = config.get(num, 'password')
    start = config.get(num, 'api_start')
    
    try:
        result = await Node.start_node(host, pas, start)
        logging.info(result)
    except Exception as ex:
        logging.error(ex)
        result = 'Something gone wrong'
    await query.message.answer(
        f'*Status*: {result["status"]}',
        reply_markup=add_cancel_button(),
        parse_mode='Markdown'
    )

async def stop_node(query: types.CallbackQuery):
    
    await query.answer()  # to remove clock sign at button
    await query.message.answer(
        'Stopping node...',
        reply_markup=add_cancel_button(),
        parse_mode='Markdown'
    )
    num = query.data.split('_')[1]
    host = config.get(num, 'ip')
    pas = config.get(num, 'password')
    stop = config.get(num, 'api_stop')
    
    try:
        result = await Node.start_node(host, pas, stop)
        logging.info(result)
    except Exception as ex:
        logging.error(ex)
        result = 'Something gone wrong'
    await query.message.answer(
        f'*Status*: {result["status"]}',
        reply_markup=add_cancel_button(),
        parse_mode='Markdown'
    )