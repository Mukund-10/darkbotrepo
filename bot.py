import discord
from discord.ext import command

Token = "NTQ5MDk4Nzg5NjcyMDU4ODgz.D1O9NQ.FZTbHQilax4M5KNtajDICjjUh6A"

client = commands.Bot(command_prefix ='d!')

@client.event
async def on_ready();
     await client.change_presence(game=discord.Game(name='beta test'))
     print('Bot is ready')

 client.run(TOKEN)
