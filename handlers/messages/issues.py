import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards.basic import make_start_keyboard, start_node_button, stop_node_button
from handlers.messages.utils import Node
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

logging.basicConfig(
    filename= 'node_request.log',
    filemode= 'w',
    encoding="utf-8",
    format='%(asctime)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)
async def my_nodes(m: Message, state: FSMContext):
    await state.finish()
    await m.answer(
        'Please wait, picking up data...',
        reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )
    
    try:
        result = await Node.main()
    except Exception as ex:
        logging.error(ex)
        result = 'Something going wrong'
        
    await m.answer(
        result,
        reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )

async def node_details(m: Message):
    await m.answer(
        f'Please wait, picking up node details',
        reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )
    node_num = m.text[1:]
    ip = config.get(node_num, 'ip')
    pas = config.get(node_num, 'password')
    status_url = config.get(node_num, 'api_status')
    result = await Node.connect_detail(ip, pas, status_url)
    if result['state'] == 'stopped':
        await m.answer(
            Node.clear_details_info(result, node_num),
            reply_markup=start_node_button(node_num),
            parse_mode='Markdown'
        )
    else:
        await m.answer(
            Node.clear_details_info(result, node_num),
            reply_markup=stop_node_button(node_num),
            parse_mode='Markdown'
        )



