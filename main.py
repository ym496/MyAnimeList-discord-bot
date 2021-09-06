import discord
import os
from discord.ext import commands



intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('+'),case_insensitive=True,help_command=None,strip_after_prefix=True)

cogs = ['cogs.search','cogs.character','cogs.meta']

  
@bot.event
async def on_ready():
  print('Bot started...')
  for cog in cogs:
    bot.load_extension(cog)
  return  


  

bot.run('TOKEN')
