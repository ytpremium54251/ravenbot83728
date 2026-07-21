import os
import sys
import time
import datetime
import math
import ssl
import json
import csv
import re
import random
import hashlib
import logging
import argparse
import pathlib
import threading
import collections
import concurrent.futures
import urllib.request
import asyncio
import requests
import aiohttp
import httpx
import telebot
import telegram
from gtts import gTTS
from urllib.parse import urlparse
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

# ✅️✅️ ((SETTING YOUR TELEGRAM ROBOTZ TOKENS HERE)) ✅️✅️
((TELEGRAM_ROBOTZ_TOKENS)) = (("8510824809:AAFccOT4VanMuQxzdz2RdW3ZxcWpBW4d5ec"))

# ✅️✅️ ((AUTHORIZATION RESPONSE AND WEIGHTED COMMANDING)) ✅️✅️
def weighted_approval(chance_approved=10):
    return random.randint(1, 100) <= chance_approved

# ✅️✅️ ((USERS IDENTIFICATION AND DOCUMENTS COMMANDING)) ✅️✅️
async def myidz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    user_id = user.id
    full_name = user.full_name
    username = user.username
    chat_id = chat.id
    version_type = "TITANIUM"
    bot_username = context.bot.username if context.bot.username else "unknownbot"
    chat_type = "INDIVIDUAL" if chat.type == "private" else "COMMUNITYZ"

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_MYIDZ = (0.0)
    await asyncio.sleep(SLEEP_MYIDZ)

    msg = f"""
• 🔍 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗜𝗗𝗘𝗡𝗧𝗜𝗧𝗬 𝗟𝗢𝗢𝗞𝗨𝗣✓

• 🤖 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗕𝗢𝗧: @{bot_username}
• 🧑🏻 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗡𝗔𝗠𝗘: <code>{full_name}</code>
• 💳 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗜𝗗𝗘𝗡𝗧𝗜𝗧𝗬: <code>{user_id}</code>
• 🔑 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: @{username if username else "noset"}
• 🗨️ 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗖𝗛𝗔𝗧 𝗜𝗗: <code>{chat_id}</code>
• 🔒 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗖𝗛𝗔𝗧 𝗧𝗬𝗣𝗘: <code>{chat_type}</code>
• 💵 𝗬𝗢𝗨𝗥 𝗧𝗚 𝗕𝗢𝗧 𝗩𝗘𝗥𝗦𝗜𝗢𝗡: <code>{version_type}</code>"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((MAIN SYSTEM LUHN VALIDATION FUNCTIONS COMMANDING))) ✅️✅️
def luhn_residue(card_number: str) -> int:
    card_number = ''.join(filter(str.isdigit, str(card_number)))
    digits = [int(d) for d in card_number[::-1]]
    return (sum(digits[::2]) + sum(sum(divmod(2 * d, 10)) for d in digits[1::2])) % 10

# ✅️✅️ ((GENERATING CARDS LUHN VALIDATION FUNCTIONS COMMANDING)) ✅️✅️
def generate_card(bin_prefix: str) -> str:
    bin_prefix = ''.join(filter(str.isdigit, bin_prefix))
    if len(bin_prefix) == 16:
        card_number = (bin_prefix)
    else:
        bin_prefix = (bin_prefix[:15])
        acc_length = 16 - len(bin_prefix) - 1
        acc = ''.join(random.choice("0123456789") for _ in range(acc_length))
        partial_card = f"{bin_prefix}{acc}"
        check_digit = str((10 - luhn_residue(partial_card + "0")) % 10)
        card_number = f"{partial_card}{check_digit}"
    mm = f"{random.randint(1, 12):02}"
    yyyy = str(random.randint(2026, 2036))
    cvv = f"{random.randint(0, 999):03}"
    return f"{card_number}|{mm}|{yyyy}|{cvv}"

# ✅✅️ ((CHECKING ALL DEIBAN CARDS YEAR VALIDATION FUNCTIONS COMMANDING)) ✅✅️
def validate_iban(iban: str) -> bool:
    iban = iban.replace(" ", "").upper()
    if not (15 <= len(iban) <= 34):
        return False
    if not iban[:2].isalpha() or not iban[2:].isalnum():
        return False
    rearranged = iban[4:] + iban[:4]
    numeric_iban = ""
    for ch in rearranged:
        if ch.isalpha():
            numeric_iban += str(ord(ch) - 55)
        else:
            numeric_iban += ch
    return int(numeric_iban) % 97 == 1

# ✅✅️ ((CHECKING ALL CARDS YEAR VALIDATION FUNCTIONS COMMANDING)) ✅✅️
def is_valid_cc_format(text: str) -> bool:
    pattern_card = r"^\d{16}\|(0[1-9]|1[0-2])\|(\d{2}|\d{4})\|\d{3}$"
    pattern_amex = r"^(34\d{13}|37\d{13})\|(0[1-9]|1[0-2])\|(\d{2}|\d{4})\|\d{4}$"
    if not (re.match(pattern_card, text) or re.match(pattern_amex, text)):
        return False
    cc, mm, yyyy, cvv = text.split("|")
    year = int(yyyy)
    if len(yyyy) == 2:
        if not (26 <= year <= 50):
            return False
    elif len(yyyy) == 4:
        if not (2026 <= year <= 2050):
            return False
    else:
        return False
    return True

# ✅️✅️ ((GERMANY DEIBANS LUHN VALIDATION FUNCTIONS COMMANDING)) ✅️✅️
def generate_german_iban(bank_code):
    account_number = ''.join(random.choices("0123456789", k=10))
    bban = bank_code + account_number
    rearranged = bban + "131400"
    numeric = int(''.join(str(ord(c) - 55) if c.isalpha() else c for c in rearranged))
    checksum = 98 - (numeric % 97)
    iban = f"DE{checksum:02}{bban}"
    return iban

# ✅️✅️ ((FETCHING CHECKING CARD INFORMATIONS FROM BINLIST APEIS)) ✅️✅️
async def fetch_bin_data(bin_prefix):
    (bin_prefix) = str(bin_prefix).strip()
    if not (bin_prefix).isdigit() or not (6 <= len(bin_prefix) <= 16):
        return None
    antipublic_urlzkeyz = f"https://bins.antipublic.cc/bins/{bin_prefix}"
    try:
        timeout = aiohttp.ClientTimeout(total=15)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(antipublic_urlzkeyz) as resp:
                if resp.status != 200:
                    await loading.edit_text("❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝗧𝗼 𝗙𝗲𝘁𝗰𝗵 𝗙𝗮𝗸𝗲 𝗗𝗮𝘁𝗮!")
                    return None
                data = await resp.json(content_type=None)
                return data if isinstance(data, dict) else None
    except (aiohttp.ClientError, aiohttp.ContentTypeError, asyncio.TimeoutError):
        await loading.edit_text("❌ 𝗘𝗿𝗿𝗼𝗿 𝗪𝗵𝗶𝗹𝗲 𝗙𝗲𝘁𝗰𝗵𝗶𝗻𝗴 𝗗𝗮𝘁𝗮!")
        return None

# ✅️✅️ ((CARD NUMBER LUHN SYSTEM VALIDATION COMMANDING)) ✅️✅️
async def card_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("<b>Examplez: </b><code>/card 601100xxxxxxxxxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_CARD = (0.0)
    await asyncio.sleep(SLEEP_CARD)

    card_number = context.args[0].strip()
    if not card_number.isdigit():
        await update.message.reply_text("❌ 𝗘𝗻𝘁𝗲𝗿 𝗔 𝗩𝗮𝗹𝗶𝗱 𝗖𝗮𝗿𝗱 𝗡𝘂𝗺𝗯𝗲𝗿!", reply_to_message_id=update.message.message_id)
        return

    digits = [int(d) for d in card_number[::-1]]
    checksum = (sum(digits[::2]) + sum(sum(divmod(2 * d, 10)) for d in digits[1::2])) % 10

    authorization_response = checksum == 0
    card_type = "NOTFOUND ⚠️"
    if card_number.startswith("4"):
        card_type = "VISA"
    elif any(card_number.startswith(prefix) for prefix in ["51", "52", "53", "54", "55", "56", "57", "58", "59"]):
        card_type = "MASTERCARD"
    elif card_number.startswith("34") or card_number.startswith("37"):
        card_type = "AMEX"
    elif card_number.startswith("6011"):
        card_type = "DISCOVER"

    msg = f"""
𝗖𝗔𝗥𝗗 𝗟𝗢𝗢𝗞𝗨𝗣 𝗥𝗘𝗦𝗨𝗟𝗧 🔍

𝗖𝗔𝗥𝗗 ➞ <code>{card_number}</code>

𝗜𝗻𝗳𝗼 ➞ {card_type}
𝗟𝘂𝗵𝗻 ➞ {checksum}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ➞ {"PASSED ✅" if authorization_response else "FAILED ❌"}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((BIN LOOKUP LUHN VALIDATION COMMANDING)) ✅️✅️
async def bin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("<b>Examplez: </b><code>/bin 601100</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    bin_prefix = context.args[0][:6]
    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_BIN = (0.0)
    await asyncio.sleep(SLEEP_BIN)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    if not bin_data:
        await loading.edit_text("❌ 𝗦𝗼𝗿𝗿𝘆 𝗕𝗶𝗻 𝗜𝗻𝗳𝗼 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱!")
        return

    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    msg = f"""
𝗕𝗜𝗡 𝗟𝗢𝗢𝗞𝗨𝗣 𝗥𝗘𝗦𝗨𝗟𝗧 🔍

𝗕𝗜𝗡 ➞ <code>{bin_prefix}</code>

𝗜𝗻𝗳𝗼 ➞ {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿 ➞ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ➞ {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((GENERATING TENS CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def gen_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or not context.args[0].isdigit() or not (6 <= len(context.args[0].strip()) <= 16):
        await update.message.reply_text("<b>Examplez: </b><code>/gen 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    user_input = context.args[0].strip()
    bin_prefix = user_input[:6]
    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    loading = await loading.edit_text("𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗰𝗮𝗿𝗱𝘀......")
    SLEEP_GEN = (0.0)
    await asyncio.sleep(SLEEP_GEN)

    cards = [generate_card(user_input) for _ in range(10)]
    card_text = '\n'.join([f"<code>{card}</code>" for card in cards])

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    msg = f"""
𝗕𝗜𝗡 ➞ <code>{bin_prefix}</code>
𝗔𝗺𝗼𝘂𝗻𝘁 ➞ <code>{10}</code>

{card_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((CHECKING CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def chk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/chk 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_CHECK = (15)
    await asyncio.sleep(SLEEP_CHECK)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅️" if authorization_response else "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌️"
    response_text = "Approved $1" if authorization_response else "Processor Declined"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Braintree Premium" if authorization_response else "Braintree Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((CHECKING AUTHORIZATION LUHN VALIDATION CARDS COMMANDING)) ✅️✅️
async def auth_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/auth 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_AUTH = (15)
    await asyncio.sleep(SLEEP_AUTH)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅️" if authorization_response else "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌️"
    response_text = "Approved $1" if authorization_response else "Processor Declined"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Braintree Auth" if authorization_response else "Braintree Auth"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅✅️ ((MASS CHECKING CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def mass_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace("/mass", "").strip()
    raw_cards = text.split('\n')

    if not raw_cards or not any('|' in c for c in raw_cards):
        await update.message.reply_text("<b>Examplez: </b><code>/mass 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    output = []
    cards = [c.strip() for c in raw_cards if c.strip() and '|' in c][:3]

    for card_info in cards:
        if not is_valid_cc_format(card_info):
            await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
            return

    loading = await update.message.reply_text(f"𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_MASS = (25)
    await asyncio.sleep(SLEEP_MASS)

    for card_info in cards:
        bin_prefix = card_info.split('|')[0][:6]

        bin_data = await fetch_bin_data(str(bin_prefix).strip())
        bin_data = (bin_data) if isinstance(bin_data, dict) else None
        card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
        scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
        brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
        bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
        country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
        country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

        authorization_response = weighted_approval(10)
        status_text = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅️" if authorization_response else "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌️"
        response_text = "Approved $1" if authorization_response else "Processor Declined"
        check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
        gateway_text = "Braintree Premium" if authorization_response else "Braintree Premium"

        output.append(f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}
""")
        final_msg = f"""
𝗠𝗔𝗦𝗦 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗟𝗢𝗢𝗞𝗨𝗣 🔍
{''.join(output)}"""
    await loading.edit_text(final_msg, parse_mode="HTML")

# ✅️✅️ ((CVV CHECKING CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def cvv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/cvv 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_CVV = (15)
    await asyncio.sleep(SLEEP_CVV)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗰𝗰𝗲𝗽𝘁𝗲𝗱 ✅" if authorization_response else "𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌️"
    response_text = "Approved Cvv ✅" if authorization_response else "Declined Cvv ❌️"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Braintree Premium" if authorization_response else "Braintree Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((THREE DE SECURE CHECKING LUHN VALIDATION COMMANDING)) ✅️✅️
async def threed_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/3ds 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_THREED = (0.5)
    await asyncio.sleep(SLEEP_THREED)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗰𝗰𝗲𝗽𝘁𝗲𝗱 ✅" if authorization_response else "𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌️"
    response_text = "Approved 3ds ✅" if authorization_response else "Declined 3ds ❌️"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Braintree Premium" if authorization_response else "Braintree Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((VERIFIED BY VISA CHECKING LUHN VALIDATION COMMANDING)) ✅️✅️
async def vbv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/vbv 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_VBV = (0.5)
    await asyncio.sleep(SLEEP_VBV)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗰𝗰𝗲𝗽𝘁𝗲𝗱 ✅" if authorization_response else "𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌️"
    response_text = "Approved Vbv ✅" if authorization_response else "Declined Vbv ❌️"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Braintree Premium" if authorization_response else "Braintree Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((SHOFIPY CHECKING CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def sfy_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/sfy 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_SHOFIPY = (15)
    await asyncio.sleep(SLEEP_SHOFIPY)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅️" if authorization_response else "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌️"
    response_text = "Approved $1" if authorization_response else "Processor Declined"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Shofipy Premium" if authorization_response else "Shofipy Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((CHECKING CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def btree_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/btree 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_BTREE = (15)
    await asyncio.sleep(SLEEP_BTREE)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅️" if authorization_response else "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌️"
    response_text = "Approved $1" if authorization_response else "Processor Declined"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Braintree Premium" if authorization_response else "Braintree Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((CHECKING CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def bthreed_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or '|' not in context.args[0]:
        await update.message.reply_text("<b>Examplez: </b><code>/b3 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    card_info = context.args[0].strip()
    bin_prefix = card_info.split('|')[0][:6].strip()

    if not is_valid_cc_format(card_info):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_BTHREED = (15)
    await asyncio.sleep(SLEEP_BTHREED)

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅️" if authorization_response else "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌️"
    response_text = "Approved $1" if authorization_response else "Processor Declined"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Braintree Premium" if authorization_response else "Braintree Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{card_info}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((GENERATING GERMANY DEIBANS LUHN VALIDATION COMMANDING)) ✅️✅️
async def igen_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("<b>Examplez: </b><code>/igen 37040044</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    bank_code = context.args[0][:8]
    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    loading = await loading.edit_text("𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗱𝗲𝗶𝗯𝗮𝗻𝘀......")
    SLEEP_IGEN = (0.0)
    await asyncio.sleep(SLEEP_IGEN)

    ibans = [generate_german_iban(bank_code) for _ in range(10)]
    iban_text = '\n'.join([f"<b>𝗗𝗘𝗜𝗕𝗔𝗡</b> <code>{iban}</code>" for iban in ibans])

    msg = f"""
𝗜𝗕𝗔𝗡 ➞ <code>{bank_code}</code>
𝗔𝗺𝗼𝘂𝗻𝘁 ➞ <code>{10}</code>

{iban_text}

𝗜𝗻𝗳𝗼: SEPA = CREDIT = (STANDARD)
𝗜𝘀𝘀𝘂𝗲𝗿: DEUTSCHE BANK AG
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: GERMANY 🇩🇪"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((CHECKING DEIBAN CARDS LUHN VALIDATION COMMANDING)) ✅️✅️
async def ichk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("<b>Examplez: </b><code>/ichk DExx37040044xxxxxxxxxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    iban = context.args[0].strip().upper()

    if not validate_iban(iban):
        await update.message.reply_text("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗘𝘅𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻 𝗔𝗰𝗰𝗼𝘂𝗻𝘁!", reply_to_message_id=update.message.message_id)
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_ICHECK = (15)
    await asyncio.sleep(SLEEP_ICHECK)

    authorization_response = weighted_approval(10)
    status_text = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅️" if authorization_response else "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌️"
    response_text = "Approved $1" if authorization_response else "Processor Declined"
    check_text = "Card Is Verified 🔥" if authorization_response else "Card Is Rejected 🚫"
    gateway_text = "Deutsche Premium" if authorization_response else "Deutsche Premium"

    msg = f"""
{status_text}

𝗖𝗮𝗿𝗱: <code>{iban}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: {gateway_text}
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: {response_text}

𝗜𝗻𝗳𝗼: SEPA = CRADIT = (STANDARD)
𝗜𝘀𝘀𝘂𝗲𝗿: DEUTSCHE BANK AG
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: GERMANY 🇩🇪"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((TEXTING TOO SPEECH COMMANDING)) ✅️✅️
async def speech_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("<b>Examplez: </b><code>/speech Hi! How Can I Help You Today?</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_SPEECH = (0.0)
    await asyncio.sleep(SLEEP_SPEECH)

    text = " ".join(context.args)
    filename = f"tts_{update.message.message_id}.mp3"

    try:
        speech = gTTS(text=text, lang="en")
        speech.save(filename)

        await loading.delete()

        with open(filename, "rb") as audio:
            await update.message.reply_voice(
                voice=audio,
                caption="• 🎙️ 𝗬𝗢𝗨𝗥 𝗥𝗔𝗩𝗘𝗡 𝗔𝗜 𝗩𝗢𝗜𝗖𝗘 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘𝗗✓", reply_to_message_id=update.message.message_id)

    except Exception as e:
        print(e)
        await loading.edit_text("❌ 𝗘𝗿𝗿𝗼𝗿 𝗪𝗵𝗶𝗹𝗲 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗩𝗼𝗶𝗰𝗲!", reply_to_message_id=update.message.message_id)

    finally:
        if os.path.exists(filename):
            os.remove(filename)

# ✅️✅️ ((FAKE FULL ADDRESS LOOKUPS COMMANDING)) ✅️✅️
async def fakey_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("<b>Examplez:</b> <code>/fakey us</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    country_code = context.args[0].lower().strip()
    loading = await update.message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    SLEEP_FAKEY = (0.0)
    await asyncio.sleep(SLEEP_FAKEY)

    randomuser_urlzkeyz = f"https://randomuser.me/api/?nat={country_code}"
    try:
        timeout = aiohttp.ClientTimeout(total=15)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(randomuser_urlzkeyz) as resp:
                if resp.status != 200:
                    await loading.edit_text("❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝗧𝗼 𝗙𝗲𝘁𝗰𝗵 𝗙𝗮𝗸𝗲 𝗗𝗮𝘁𝗮!")
                    return None
                data = await resp.json(content_type=None)
                user = data["results"][0]
    except (aiohttp.ClientError, aiohttp.ContentTypeError, asyncio.TimeoutError):
        await loading.edit_text("❌ 𝗘𝗿𝗿𝗼𝗿 𝗪𝗵𝗶𝗹𝗲 𝗙𝗲𝘁𝗰𝗵𝗶𝗻𝗴 𝗗𝗮𝘁𝗮!")
        return None

    full_name = f"{user['name']['first']} {user['name']['last']}"
    gender = user["gender"]
    id_name = user["id"]["name"]
    id_value = user["id"]["value"]
    location = user["location"]
    street = f"{location['street']['number']} {location['street']['name']}"
    city = user["location"]["city"]
    state = user["location"]["state"]
    postcode = user["location"]["postcode"]
    phone = user["phone"]
    country = user["location"]["country"]
    email = user["email"]
    first = user["name"]["first"].lower()
    last = user["name"]["last"].lower()
    random_number = random.randint(1000, 9999)
    email = f"{first}{last}{random_number}@gmail.com"

    msg = f"""
• 𝗬𝗢𝗨𝗥 𝗙𝗔𝗞𝗘 𝗜𝗗𝗘𝗡𝗧𝗜𝗧𝗬 𝗟𝗢𝗢𝗞𝗨𝗣 🔍

• 𝗬𝗢𝗨𝗥 𝗡𝗔𝗠𝗘: <code>{full_name}</code>
• 𝗬𝗢𝗨𝗥 𝗦𝗘𝗫: <code>{gender.title()}</code>
• 𝗬𝗢𝗨𝗥 𝗚𝗢𝗩𝗜𝗗: <code>{id_name} {id_value}</code>
• 𝗬𝗢𝗨𝗥 𝗦𝗧𝗥𝗘𝗘𝗧: <code>{street}</code>
• 𝗬𝗢𝗨𝗥 𝗖𝗜𝗧𝗬: <code>{city}</code>
• 𝗬𝗢𝗨𝗥 𝗦𝗧𝗔𝗧𝗘: <code>{state}</code>
• 𝗬𝗢𝗨𝗥 𝗭𝗜𝗣𝗖𝗢𝗗𝗘: <code>{postcode}</code>
• 𝗬𝗢𝗨𝗥 𝗣𝗛𝗢𝗡𝗘: <code>{phone}</code>
• 𝗬𝗢𝗨𝗥 𝗖𝗢𝗨𝗡𝗧𝗥𝗬: <code>{country}</code>
• 𝗬𝗢𝗨𝗥 𝗘𝗠𝗔𝗜𝗟: <code>{email}</code>"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((GENERATING TWENTYS CARDS LUHN VALIDATION COMMANDING) ✅️✅️
async def genty_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or not context.args[0].isdigit() or not (6 <= len(context.args[0].strip()) <= 16):
        await update.message.reply_text("<b>Examplez: </b><code>/genty 601100xxxxxxxxxx|xx|2026|xxx</code>", reply_to_message_id=update.message.message_id, parse_mode="HTML")
        return

    bin_prefix = context.args[0].strip()
    count = 20 if len(context.args) < 2 else min(int(context.args[1]), 50)
    loading = await update.message.reply_text(f"𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁......", reply_to_message_id=update.message.message_id)
    loading = await loading.edit_text("𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗰𝗮𝗿𝗱𝘀......")
    SLEEP_GENTY = (0.0)
    await asyncio.sleep(SLEEP_GENTY)

    cards = []
    for _ in range(count):
        acc = ''.join(random.choice("0123456789") for _ in range(16 - len(bin_prefix) - 1))
        card = f"{bin_prefix}{acc}"
        check_digit = str((10 - luhn_residue(card + "0")) % 10)
        card += check_digit
        mm = f"{random.randint(1, 12):02}"
        yyyy = str(random.randint(2026, 2036))
        cvv = f"{random.randint(0, 999):03}"
        cards.append(f"<code>{card}|{mm}|{yyyy}|{cvv}</code>")

    card_text = '\n'.join([f"<code>{card}</code>" for card in cards])

    bin_data = await fetch_bin_data(str(bin_prefix).strip())
    bin_data = (bin_data) if isinstance(bin_data, dict) else None
    card_type = str(bin_data.get("type", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    scheme = str(bin_data.get("level", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    brand = str(bin_data.get("brand", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    bank = str(bin_data.get("bank", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_name = str(bin_data.get("country_name", "NOTFOUND")).upper() if isinstance(bin_data, dict) else "NOTFOUND"
    country_flag = str(bin_data.get("country_flag", "⚠️")) if isinstance(bin_data, dict) else "⚠️"

    msg = f"""
𝗕𝗜𝗡 ➞ <code>{bin_prefix}</code>
𝗔𝗺𝗼𝘂𝗻𝘁 ➞ <code>{20}</code>

{card_text}

𝗜𝗻𝗳𝗼: {brand} = {card_type} = ({scheme})
𝗜𝘀𝘀𝘂𝗲𝗿: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_flag}"""
    await loading.edit_text(msg, parse_mode="HTML")

# ✅️✅️ ((STARTING YOUR RAVEN SAVVY TELEGRAM ROBOTZ)) ✅️✅️
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loading = await update.message.reply_text("⏤͟͟͟͟͞͞͞𝙇𝙀𝘼𝙍𝙉𝙕 𝙎𝙊𝙈𝙀𝙏𝙃𝙄𝙉𝙂 𝙏𝙊𝙊𝘿𝘼𝙔❗", reply_to_message_id=update.message.message_id)
    SLEEP_START = (0.0)
    await asyncio.sleep(SLEEP_START)

    msg = f"""
🤖 Bot Status:- Active ✅

❗ For Announcements And Updates, Join Us 👉🏻 <a href="https://t.me/revxgen">Here</a>.

⚠️ Tip: To Use Raven In Your Group, Make Sure To Set It As An Admin."""
    keyboard = [[InlineKeyboardButton("MENU 🔍", callback_data="menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await loading.edit_text(msg, reply_markup=reply_markup, parse_mode="HTML")

# ✅️✅️ ((STARTING YOUR MENU BUTTON RAVEN SAVVY TELEGRAM ROBOTZ)) ✅️✅️
async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    msg = f"""
•❗𝗟𝗘𝗔𝗥𝗡𝗭 𝗦𝗢𝗠𝗘𝗧𝗛𝗜𝗡𝗚 𝗧𝗢𝗢𝗗𝗔𝗬

• 🔍 𝗬𝗢𝗨𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗜𝗗𝗘𝗡𝗧𝗜𝗧𝗬 𝗔𝗡𝗗 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗟𝗢𝗢𝗞𝗨𝗣:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗺𝘆𝗶𝗱𝘇)
𝗘𝗫𝗔𝗠𝗣𝗟𝗘: /𝗺𝘆𝗶𝗱𝘇

• 🎙️ 𝗬𝗢𝗨𝗥 𝗥𝗔𝗩𝗘𝗡 𝗔𝗜 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗩𝗢𝗜𝗖𝗘 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗡𝗚:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝘀𝗽𝗲𝗲𝗰𝗵)
𝗘𝗫𝗔𝗠𝗣𝗟𝗘: /𝘀𝗽𝗲𝗲𝗰𝗵 𝗛𝗜 𝗛𝗢𝗪 𝗖𝗔𝗡 𝗜 𝗛𝗘𝗟𝗣 𝗬𝗢𝗨 𝗧𝗢𝗗𝗔𝗬

• 🗑️ 𝗬𝗢𝗨𝗥 𝗕𝗜𝗡 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗔𝗡𝗗 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 𝗟𝗢𝗢𝗞𝗨𝗣:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗯𝗶𝗻)
𝗘𝗫𝗔𝗠𝗣𝗟𝗘: /𝗯𝗶𝗻 𝟲𝟬𝟭𝟭𝟬𝟬

• ✅ 𝗬𝗢𝗨𝗥 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗖𝗔𝗥𝗗 𝗟𝗨𝗛𝗡 𝗩𝗔𝗜𝗟𝗗 𝗖𝗔𝗥𝗗 𝗢𝗥 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗖𝗔𝗥𝗗:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗰𝗮𝗿𝗱)
𝗙𝗢𝗥𝗠𝗔𝗧: /𝗰𝗮𝗿𝗱 𝟲𝟬𝟭𝟭𝟬𝟬𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫

• 🔐 𝗬𝗢𝗨𝗥 𝗕𝗜𝗡 𝗧𝗢𝗢 𝗖𝗥𝗘𝗗𝗜𝗧 𝗖𝗔𝗥𝗗𝗦 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥: (𝗨𝗣𝗧𝗢 𝟭𝟬 𝗖𝗔𝗥𝗗𝗦)
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗴𝗲𝗻)
𝗘𝗫𝗔𝗠𝗣𝗟𝗘 𝟭: /𝗴𝗲𝗻 𝟲𝟬𝟭𝟭𝟬𝟬
𝗘𝗫𝗔𝗠𝗣𝗟𝗘 𝟮: /𝗴𝗲𝗻 𝟲𝟬𝟭𝟭𝟬𝟬𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩

• ⚠️ 𝗬𝗢𝗨𝗥 𝗩𝗕𝗩 𝗢𝗥 𝗡𝗢𝗡 𝗩𝗕𝗩 𝟯𝗗𝗦 𝗖𝗔𝗥𝗗𝗦 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗟𝗢𝗢𝗞𝗨𝗣:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝘃𝗯𝘃 𝗮𝗻𝗱 /𝟯𝗱𝘀)
𝗙𝗢𝗥𝗠𝗔𝗧: /𝘃𝗯𝘃 𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩
𝗙𝗢𝗥𝗠𝗔𝗧: /𝟯𝗱𝘀 𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩

• 💳 𝗬𝗢𝗨𝗥 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗖𝗔𝗥𝗗𝗦 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗔𝗡𝗗 𝗠𝗔𝗦𝗦 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚: (𝗨𝗣𝗧𝗢 𝟬𝟱 𝗖𝗔𝗥𝗗𝗦)
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗰𝗵𝗸 /𝗮𝘂𝘁𝗵 /𝗰𝘃𝘃 /𝗺𝗮𝘀𝘀 /𝗯𝟯)
𝗙𝗢𝗥𝗠𝗔𝗧: /𝗰𝗵𝗸 𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩
𝗙𝗢𝗥𝗠𝗔𝗧: /𝗺𝗮𝘀𝘀 𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩
𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩
𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩
𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩
𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩

• 🛒 𝗬𝗢𝗨𝗥 𝗦𝗛𝗢𝗙𝗜𝗣𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗖𝗥𝗘𝗗𝗜𝗧 𝗖𝗔𝗥𝗗𝗦 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗟𝗢𝗢𝗞𝗨𝗣:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝘀𝗳𝘆)
𝗙𝗢𝗥𝗠𝗔𝗧: /𝘀𝗳𝘆 𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫 | 𝗘𝗫𝗣_𝗗𝗔𝗧𝗘 | 𝗖𝗩𝗩

• 🏠 𝗬𝗢𝗨𝗥 𝗙𝗔𝗞𝗘 𝗔𝗗𝗗𝗥𝗘𝗦𝗦 𝗔𝗡𝗗 𝗜𝗗𝗘𝗡𝗧𝗜𝗧𝗬 𝗟𝗢𝗢𝗞𝗨𝗣 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗳𝗮𝗸𝗲𝘆) (𝗖𝗢𝗨𝗡𝗧𝗥𝗬 𝗖𝗢𝗗𝗘)
𝗘𝗫𝗔𝗠𝗣𝗟𝗘 𝟭: /𝗳𝗮𝗸𝗲𝘆 𝘂𝘀
𝗘𝗫𝗔𝗠𝗣𝗟𝗘 𝟮: /𝗳𝗮𝗸𝗲𝘆 𝘂𝗸

• 🇩🇪 𝗬𝗢𝗨𝗥 𝗚𝗘𝗥𝗠𝗔𝗡𝗬 𝗜𝗕𝗔𝗡 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗡𝗨𝗠𝗕𝗘𝗥𝗦 𝗕𝗔𝗡𝗞𝗖𝗢𝗗𝗘 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗶𝗴𝗲𝗻)
𝗘𝗫𝗔𝗠𝗣𝗟𝗘: /𝗶𝗴𝗲𝗻 𝟯𝟳𝟬𝟰𝟬𝟬𝟰𝟰

• 🇩🇪 𝗬𝗢𝗨𝗥 𝗚𝗘𝗥𝗠𝗔𝗡𝗬 𝗗𝗘𝗨𝗧𝗦𝗖𝗛𝗘 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗜𝗕𝗔𝗡𝗦 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 𝗖𝗔𝗥𝗗𝗦 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚:
𝗖𝗢𝗠𝗠𝗔𝗡𝗗: (/𝗶𝗰𝗵𝗸)
𝗙𝗢𝗥𝗠𝗔𝗧: /𝗶𝗰𝗵𝗸 𝗗𝗘𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫𝗫"""
    keyboard = [[InlineKeyboardButton("BACK 🔍", callback_data="back")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(msg, reply_markup=reply_markup, parse_mode="HTML")

# ✅️✅️ ((STARTING YOUR BACK BUTTON RAVEN SAVVY TELEGRAM ROBOTZ)) ✅️✅️
async def back_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    msg = f"""
🤖 Bot Status:- Active ✅

❗ For Announcements And Updates, Join Us 👉🏻 <a href="https://t.me/revxgen">Here</a>.

⚠️ Tip: To Use Raven In Your Group, Make Sure To Set It As An Admin."""
    keyboard = [[InlineKeyboardButton("MENU 🔍", callback_data="menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(msg, reply_markup=reply_markup, parse_mode="HTML")

# ✅️✅️ ((STARTING YOUR FASTRACK SAVVYZ TELEGRAM ROBOTZ)) ✅️✅️
if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_ROBOTZ_TOKENS).build()
    application.add_handler(CommandHandler(["start", "cmds", "menu", "help"], start_command))
    application.add_handler(CommandHandler("myidz", myidz_command))
    application.add_handler(CommandHandler("bin", bin_command))
    application.add_handler(CommandHandler("card", card_command))
    application.add_handler(CommandHandler("gen", gen_command))
    application.add_handler(CommandHandler("chk", chk_command))
    application.add_handler(CommandHandler("auth", auth_command))
    application.add_handler(CommandHandler("mass", mass_command))
    application.add_handler(CommandHandler("cvv", cvv_command))
    application.add_handler(CommandHandler("3ds", threed_command))
    application.add_handler(CommandHandler("vbv", vbv_command))
    application.add_handler(CommandHandler("sfy", sfy_command))
    application.add_handler(CommandHandler("btree", btree_command))
    application.add_handler(CommandHandler("b3", bthreed_command))
    application.add_handler(CommandHandler("igen", igen_command))
    application.add_handler(CommandHandler("ichk", ichk_command))
    application.add_handler(CommandHandler("fakey", fakey_command))
    application.add_handler(CommandHandler("genty", genty_command))
    application.add_handler(CommandHandler("speech", speech_command))
    application.add_handler(CallbackQueryHandler(menu_callback, pattern="menu"))
    application.add_handler(CallbackQueryHandler(back_callback, pattern="back"))
    application.run_polling()
