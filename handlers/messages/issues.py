
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards.basic import make_start_keyboard
from handlers.messages.utils import Connection

async def my_nodes(m: Message, state: FSMContext):
    await state.finish()
    await m.answer(
        'Please wait, picking up data...',
        reply_markup=make_start_keyboard(),
        parse_mode='Markdown'
    )
    nodes = 200
    result = await Connection.main()
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



