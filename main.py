import wikipedia
import re
import discord
from config import TOKEN
client = discord.Client()

pattern = r'\-p (.*)'
prog = re.compile(pattern)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-p'):
        result = prog.match(message.content)
        wikiSearch= wikipedia.summary(result.group(1))

        await message.channel.send(wikiSearch[:2000])

client.run(TOKEN)