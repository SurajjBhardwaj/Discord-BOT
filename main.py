import discord
import os

intents = discord.Intents.default()
# intents.messages = True  # Enable the messages intent (needed for on_message event)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("hey", message.content)  # Proper indentation
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

client.run(os.environ['TOKEN'])
