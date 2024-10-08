import asyncio
import sys
from datetime import datetime
from os import environ, execle

from pytz import timezone

from ErUbot import LOGGER, bot, ubot
from ErUbot.config import SKY
from ErUbot.utils.dbfunctions import *
from ErUbot.utils.ultra import *


async def expired_date():
    while True:
        now = datetime.now(timezone("Asia/Jakarta"))
        time = now.strftime("%d-%m-%Y")
        clock = now.strftime("%H:%M:%S")
        for X in ubot._ubot:
            try:
                exp = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")
                if time == exp:
                    await X.log_out()
                    await rem_expired_date(X.me.id)
                    await remove_ultraprem(X.me.id)
                    await remove_ubot(X.me.id)
                    ubot._ubot.remove(X)
                    await bot.send_message(
                        SKY,
                        f"<b>{X.me.first_name} {X.me.last_name or ''} | <code>{X.me.id}</code> masa aktif telah habis</b>",
                    )
            except:
                pass