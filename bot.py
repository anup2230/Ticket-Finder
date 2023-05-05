import discord, os, ticket_finder, time

TOKEN = 'MTEwMzU5MTEwNzgzNDY4MzM5Mg.GzSNGD.NiX3ltS_mOIZwCvqRhBRycN2IQ0hoTyLQH3yes'
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

