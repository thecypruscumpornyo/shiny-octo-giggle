from telethon import TelegramClient, events
import json

api_id = 3029628
api_hash = '70620875a64498c57ff95faec660d758'
token = '1662624308:AAHKqIAAXohK6B1alvWjrDFzB3RORSP2eXE'

client = TelegramClient(token, api_id, api_hash) 

@client.on(events.NewMessage(pattern=r'\.컽')) 
async def nopsa(event) :
    contents = "**킥 먹은 노 프사 명단** \n"
    async for user in client.iter_participants(event.chat_id):
        if user.photo == None :
            name = ""
            if user.first_name != None : name += f"{user.first_name}"
            if user.first_name != None : name += f"{user.last_name}"
            if name == "" :
                contents += f"[Unknown](tg://user?id={user.id}) `{user.id}` \n"
            else :
                contents += f"[{name}](tg://user?id={user.id}) `{user.id}` \n"
            await client.kick_participant(event.chat_id, user.id)
    await client.send_message(event.chat_id, contents)
            

client.start()
client.run_until_disconnected()
	

