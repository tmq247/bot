#
# Copyright (C) 2023-2024 by TeamScary@Github, < https://github.com/TeamScary >.
#
# This file is part of < https://github.com/TeamScary/Ai-UserBot > project,
#
# All rights reserved.

from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from os import getenv
import re
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", None)
MONGO_URL = getenv("MONGO_URL", None)

client = Client(SESSION_NAME, API_ID, API_HASH)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in client.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    scaryai = await message.reply("👀")
    await asyncio.sleep(1)
    await scaryai.edit("**ʀᴇᴘᴏ ᴛᴏ ᴘʀɪᴠᴀᴛᴇ ʜᴀ ʙᴜᴅᴅʜᴜ 👉👈😁**")
    await asyncio.sleep(1)
    await scaryai.edit("**ᴄʜᴀʟᴏ ᴀʙ ᴋɪssɪ ᴅᴏ 🙈🥰**")
    await scaryai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgEAAxkBAAICOGPkoH1fKzKpaISh7XgNeisx3UVVAAK1AwACKWtwRmr9H9xzpEZDLgQ")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9026db38f6f7fa66c32c9.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━
🥀 ᴀ ᴘᴏᴡᴇʀғᴜʟʟ ᴀɪ ʙᴏᴛ ᴏғ [Lᴀᴋsʜʏᴀ](https://t.me/SayJust) 🌺🌟
━━━━━━━━━━━━━━━━━━━
ᴅᴀᴛᴀʙᴀsᴇ ʙᴀᴄᴋᴇɴᴅ ʙᴏᴛ ғᴏʀ ᴛɢ..
┏━━━━━━━━━━━━━━━━━┓
┣× ᴏᴡɴᴇʀ ☞ [Sᴏᴏɴ](https://t.me/Toxic_ixi)
┣× sᴜʙsᴄʀɪʙᴇ ᴏɴ ☞ [ʏᴏᴜᴛᴜʙᴇ](https://youtube.com/@LakshyaisLive)
┣× sᴜᴘᴘᴏʀᴛ ☞ [sᴜᴘᴘᴏʀᴛ](https://t.me/ScaryNetwork)
┣× ᴜᴘᴅᴀᴛᴇs ☞ [ᴜᴘᴅᴀᴛᴇs](https://t.me/ScaryServer)
┣× sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ☞ [ʜᴇʀᴇ](https://github.com/TheTeamScary/Ai-UserBot)
┣× ᴄʀᴇᴀᴛᴏʀ ☞ [Nᴏᴏʙ](https://t.me/NomoreLakshya)
┗━━━━━━━━━━━━━━━━━┛
🥀  ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴ ᴛʜᴇɴ ɢᴏ ᴛᴏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ [Hᴇʟᴘ](https://t.me/chat_ixz)**""",
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**ᴄᴜᴛɪᴇ ᴜsᴇʀʙᴏᴛ ɪs ʀᴇᴀᴅʏ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ**")

@client.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    scarydb = MongoClient(MONGO_URL)    
    scary = scarydb["ScaryDb"]["Scary"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                ""
            )
    is_scary = scary.find_one({"chat_id": message.chat.id})
    if not is_scary:
        scary.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"**ᴄʜᴀᴛʙɪᴛ ɪs ᴅɪsᴀʙʟᴇᴅ ʙʏ {message.from_user.mention()} ғᴏʀ ᴜsᴇʀs ɪɴ {message.chat.title}**")
    if is_scary:
        await message.reply_text(f"**ᴄʜᴀᴛʙɪᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ**")
    

@client.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    scarydb = MongoClient(MONGO_URL)    
    scary = scarydb["ScaryDb"]["Scary"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ"
            )
    is_scary = scary.find_one({"chat_id": message.chat.id})
    if not is_scary:           
        await message.reply_text(f"**ᴄʜᴀᴛʙɪᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ**")
    if is_scary:
        scary.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"**ᴄʜᴀᴛʙɪᴛ ɪs ᴇɴᴀʙʟᴇᴅ ʙʏ {message.from_user.mention()} ғᴏʀ ᴜsᴇʀs ɪɴ {message.chat.title}**")
    

@client.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴇᴀɢᴇ:**\n/chatbot [on|off] ᴏɴʟʏ ɢʀᴏᴜᴘ**")

    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scaryai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})
       if not is_scary:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_scary:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scarystickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})
       if not is_scary:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_scary:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scaryprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scaryprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
