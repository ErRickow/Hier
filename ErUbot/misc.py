from ErUbot.config import OWNER_ID
from ErUbot.utils.dbfunctions import *
from ErUbot.utils.ultra import *


async def premium():
    if OWNER_ID not in await get_seles():
        await add_seles(OWNER_ID)
    if OWNER_ID not in await get_prem():
        await add_prem(OWNER_ID)
    if OWNER_ID not in await get_ultraprem():
        await add_ultraprem(OWNER_ID)
    
