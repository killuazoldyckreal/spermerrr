import os, random, string, keep_alive
from nextcord.ext import commands, tasks

version = 'v2.7.4'

client = commands.Bot(command_prefix="&")
intervals = [2.0, 2.1, 2.2, 2.3, 2.4]

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(968611662137524275)
    await channel.send("good night")

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

spam.start()
@client.event
async def on_ready():
    print(f'Logged into account: {client.user.name}')

keep_alive.keep_alive()
client.run("NDk1NDc2NTc1NjI2NTkyMjY3.GKEq1F.-HlYClZ6gG67ti1Cv2FVirYwxcjpCtM4FfZNr0")
