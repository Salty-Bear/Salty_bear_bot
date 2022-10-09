import discord
import os
import requests
import json
import random
from discord.ext import commands
from keep_alive import keep_alive

client = discord.Client()

owner =514774593270054923
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('Salty bear has activated the bot as {0.user}'.format(client))


@client.event
async def on_message(message):
    username=str(message.author)

    
    if message.author == client.user:
        return

    if message.content.startswith(";ping"):
     await message.channel.send(f'_**Pong !!** {round(client.latency*1000,2)} **ms**_')

    if message.content.startswith("joe"):
        await message.channel.send('JOE MAMA Gay!!')

    if message.content.startswith(";quote"):
        quote = get_quote()
        await message.channel.send("_"+quote+"_")

      
    if message.content.startswith(";random"):
      ran=random.randrange(10000)
      await message.channel.send(f'Here is your random number : {ran}')
    

    if(message.channel.name == 'talk-with-namkeen-bhalu'):
      if(message.content.startswith('hello')):
        await message.channel.send(f'Hello {username}')

      if(message.content.startswith('how are you')):
        await message.channel.send('good')

      if(message.content.startswith('who is your owner')):
        await message.channel.send('my Owner is Namkeen bhalu')

      if(message.content.startswith('what do you like')):
        amanid='<@461228204405948416>'
        await message.channel.send('i like omelette and apka mom %s' % amanid)

        
        






keep_alive()
client.run(os.getenv('TOKEN'))
