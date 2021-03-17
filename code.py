from telethon import TelegramClient, events
import json

api_id = 3029628
api_hash = '70620875a64498c57ff95faec660d758'
token = '1662624308:AAHKqIAAXohK6B1alvWjrDFzB3RORSP2eXE'

client = TelegramClient(token, api_id, api_hash) 

@client.on(events.NewMessage)
async def getchat(events) :
    f = open('list.json', "r")
    json_data = json.load(f)
    user = await events.get_sender()
    try :
        json_data[str(user.id)] = json_data[str(user.id)] + 1
    except :
        user_data = {
            user.id : {
                'point' : 1
            }
        }
        json_data.update(user_data)
    with open('list.json', 'w', encoding='utf-8') as make_file:
        json.dump(json_data, make_file, indent="\t")
	make_file.close()

client.start()
client.run_until_disconnected()
	

