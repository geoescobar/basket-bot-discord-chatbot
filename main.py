import discord

TOKEN = 'ENTER YOUR TOKEN HERE'

intents = discord.Intents.default()
intents.message_content = True #v2
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    if message.author == client.user:
        return
    
    if message.channel.name == 'welcome':
        if user_message.lower() == 'hello':
            await message.channel.send(f"What's up {username}!")
            return
        
        elif user_message.lower() == "bye":
            await message.channel.send(f"See ya later, {username}!")
            return
    
    if user_message.lower() == '!anywhere':
        await message.channel.send("I see you! Talk that talk!")
        return
        



client.run(TOKEN)
