from telethon import TelegramClient, events
import json

api_id = 3029628
api_hash = '70620875a64498c57ff95faec660d758'
token = '1712942144:AAEC5L-MzB3dkGCJxUTkrJcUzHnMq2x85cA'

client = TelegramClient(token, api_id, api_hash) 

async def checkroom (userid) :
    async for user in client.iter_participants(-1001227362971) :
        if user.id == userid :
            return 1
        
@client.on(events.NewMessage(pattern=r'\/check'))
async def checkmychats (event) :
    point = "\U0001F534"
    if await checkroom(event.sender_id) == 1 : point = "\U0001F7E2"
    contents = f"{point} 무덤 가입 여부\n\U0001F7E2 봇 정상 작동 여부"
    await client.send_message(event.chat_id, contents)
	
client.start()
client.run_until_disconnected()

