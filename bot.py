import discord, os, ticket_finder, time

TOKEN = 'MTEwMzU5MTEwNzgzNDY4MzM5Mg.GWrgbw.ncodzgGtNNsYLfaD_snI5rdG7bNo10duTfM8JQ'
client = discord.Client(intents=discord.Intents.default())
CHANNEL_ID = 1103593266189975625

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.content.startswith(''):
        await message.channel.send(ticket_finder.find_tickets())
    if message.content.startswith('status'):
        await message.channel.send("I'm online(:")
    time.sleep(30)


client.run(TOKEN)

