# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available

• `{i}hack`
    Do a Prank With Replied user.

"""

import asyncio
import random

from . import *


@ultroid_cmd(pattern="hack")
async def _(event):
    animation_interval = 0.8
    animation_ttl = range(0, 11)
    xx = await event.eor("Installing..")
    animation_chars = [
        "`Installing Files To Hacked Private Server...`",
        "`Target Selected.`",
        "`Installing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`lnstalling... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 84%\n█████████████████████▒▒▒▒ `",
        "`Installing... 100%\n████████Installed██████████ `",
        "`Target files Uploading...\n\nDirecting To Remote server to hack..`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await xx.edit(animation_chars[i % 14])
    await asyncio.sleep(2)
    animation_interval = 0.8
    animation_ttl = range(0, 10)
    await xx.edit("`Connecting and getting combined token from my.telegram.org`")
    await asyncio.sleep(1)
    animation_chars = [
        "`root@anon:~#` ",
        "`root@anon:~# ls`",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~#`",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...`",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# `",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py`",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...`",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user`",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...\n\nAll Done!`",
        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...\n\nAll Done!\nInstalling Token!\nToken=`DJ65gulO90P90nlkm65dRfc8I`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await xx.edit(animation_chars[i % 14])
    await asyncio.sleep(1)
    await xx.edit("`starting tg-exploit`")
    await asyncio.sleep(1)
    await xx.edit(
        "`processing.....0% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (1.3) kB`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`processing.....4% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (1.3) kB\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`processing.....9% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (1.3) kB\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`processing....14% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`processing....26% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh installing`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`processing....32% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index`"
    )
    await asyncio.sleep(3)
    await xx.edit(
        "`processing....48% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n Bruteforce still up and running`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`processing....60% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n Bruteforce still up and running`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`processing....73% completed\n TERMINAL:\n downloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n unpacking Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n Bruteforce-Telegram-0.1 successfully installed\n Bruteforce started\n\n chat history from telegram exported to private database\n TERMINAL:\n 874379gvrfghhuu5tlotruhi5rbh succesfully installed\n creating data index\n\n Bruteforce still up and running\n\n BRUTEFORCE FOUND PASSWORD\n\n done with status 36748hdeg`"
    )
    await asyncio.sleep(1)
    await xx.edit(
        "`processing....88% completed\n ====================================\n ====================================\n scraping data from user account\n ====================================\n ====================================`"
    )
    await asyncio.sleep(5)
    await xx.edit(
        "`█████████HACKED███████████ `\n\n TERMINAL:\n tg-exploit log files stored in directory:\n emulated/0/android/apps/tg-exploit/log/`"
    )
    await asyncio.sleep(2)
    await xx.edit(
        "`█████████HACKED███████████ `\n\n TERMINAL:\n tg-exploit log files stored in directory:\n emulated/0/android/apps/tg-exploit/log/\n\n drives were cloned to database\n access via:\n\n https://grabify.link/KJJZF0.docx`"
    )
