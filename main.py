import discord

TOKEN = 'INSERT YOUR TOKEN HERE'


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
            await message.channel.send(f"What's up {username}! 🏀")
            return
        
        elif user_message.lower() == "bye":
            await message.channel.send(f"See ya later, @{username}! 👋")
            return
        
    if message.channel.name == "mavericks":
        if user_message.lower() == "Mavericks":
            await message.channel.send("#MFFL")
            return 
        
    if user_message.lower() == '!anywhere':
        await message.channel.send("What's your basketball hot take this season? 👀" )
        return
    
    if user_message.lower() == 'help':
        await message.channel.send(f"Please refer to the #help channel, @{username}")
        return
        



client.run(TOKEN)
