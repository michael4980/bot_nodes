
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards.basic import make_start_keyboard
from client import Connect_session
from data import load_config
import datetime
import asyncio
config = load_config(r"config.ini")
hosts = config.nodes.node_ips.split('\n')
pasws = config.nodes.passwords.split('\n')
apis = config.nodes.api_urls.split('\n')

def iterator():
    for host, pas, api in zip(hosts, pasws, apis):
        yield host, pas, api
    
def clear_info(result):
    if result['state'] == "stopped":
       clear_message = f"*Статус ноды:* {result['state']}\
                     \n*Adress:* {result['nominatorAddress']}\
                     \n*Message:* {result['exitMessage']}\
                     \n*StatusCode:* {result['exitStatus']}\
                     \n\n"  
    else: 
        clear_message = f"*Статус ноды:* {result['state']}\
                        \n*Adress:* {result['nominatorAddress']}\
                        \n*Last_work:* {get_time(result['lastActive'])}\
                        \n\n"                   
    return clear_message  

def get_time(time):
    if isinstance(time, int):
        dt = datetime.datetime.fromtimestamp(int(time)/1000)
        return dt
    
async def connect(host, pas, api):
    result = await Connect_session.connect(url=host, pas=pas, api=api, func = Connect_session.get_data)
    return clear_info(result)

async def main():
    res = await asyncio.gather(*(connect(host, pas, api) for host, pas, api in iterator()))
    return ''.join(str(i) for i in res)

async def my_nodes(m: Message, state: FSMContext):
    await state.finish()
    await m.answer(
        'Please wait, picking up data...',
        reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )
    nodes = 200
    result = await main()
    if nodes == 200:
        await m.answer(
            result,
            reply_markup=make_start_keyboard(),
            parse_mode='Markdown'
        )
    else:
        await m.answer(
            nodes.text,
            reply_markup=make_start_keyboard(),
            parse_mode='Markdown'
        )


async def node_details(m: Message):
    await m.answer(
        'Please wait, picking up details',
        reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )

    # issue_id = m.text[1:]
    # issue_details = await get_issue_details(issue_id)
    # await m.answer(
    #     render_order_details(issue_details),
    #     reply_markup=add_issue_buttons(issue_id),
    #     parse_mode='Markdown'
    # )



