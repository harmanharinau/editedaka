"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "You are not dead. You are still here. You have no love for me now. Okay .. you're not changed like you used to be..๐" 
HOW_TO_OWN = "<b>แดกแดแดแดส แดแดแดแดสษชแดส แดแด แดษดแดแดก สแดแดก แดแด แดแดแดแด แดแดแดแด าษชสแดแดส สแดแด โบโบ https://youtu.be/MfUjmZ1mpfc</b>"
CHANNEL = "<b>๐๐พ๐๐๐๐ฑ๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป</b> โบโบ https://youtube.com/channel/UCMzFIpsfTkZfkI-O20o1gww\n\n<b>๐๐ฟ๐ณ๐ฐ๐๐ด๐ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป โบโบ https://t.me/cynitebots</b>\n\n<b>๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป โบโบ https://t.me/cynitemovies</b>"
ZSEARCHERBOT = "<b>๐ฑ๐พ๐ โบโบ https://t.me/zsearcherbot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("how_to_own", COMMAND_HAND_LER) & f_onw_fliter)
async def how_to_own(_, message):
    await message.reply_text(HOW_TO_OWN)

@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("zsearcherbot", COMMAND_HAND_LER) & f_onw_fliter)
async def Zsearcherbot(_, message):
    await message.reply_text(ZSEARCHERBOT)


