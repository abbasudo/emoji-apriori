from telethon import TelegramClient
import asyncio
import json
import sys
sys.setrecursionlimit(10000)

#paste your api credentials from my.telegram.org
api_id = 10000
api_hash = 'api_hash'


# set the amount that you want to extract from each group
limit = 300
async def main():
 async with TelegramClient('session', api_id, api_hash) as client:
  dialogs = await client.get_dialogs()
  dialogs = [d for d in dialogs if d.is_group]
  result = []
  for dialog in dialogs:
   entity = await client.get_entity(dialog.entity)
   async for message in client.iter_messages(entity , limit = limit):
    try :
     print('{:>14}: {} : {} : {}'.format(message.id,
     message.sender.first_name , message.text , message.date))
     messageDict = message.to_dict();
     messageDict['sender'] = message.sender.to_dict()
     result.append(messageDict)
    except :
     pass

 json_object = json.dumps(result,default=str)
 with open("groups-messages-"+str(limit)+".json", "w") as outfile:
  outfile.write(json_object)
if __name__ == '__main__':
 asyncio.run(main())
