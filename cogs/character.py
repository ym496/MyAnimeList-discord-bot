import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import MissingRequiredArgument
import DiscordUtils
from cogs.getjson import jikanjson
from cogs.getname import getname
from cogs.results import results
from cogs.selection import selection

prefix = '+'

class Character_Info(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  desc = 'Gives information about a character via '+ '[MyAnimeList](https://myanimelist.net/).'
  help_command = f'`{prefix}character Mikasa Ackerman`\n`{prefix}char Oreki Houtarou`\n`{prefix}char リヴァイ`'
  @commands.command(name='character',no_pm=True,aliases=['char'],brief = 'Get Information about a character from an anime or manga.',usage=f'`{prefix}character <name>`\n`{prefix}char <name>`',description=desc,help=help_command)
  async def character(self,ctx,*,name):
    if ctx.guild:
      pass
    else:
      return
    
    query = getname(name)
    url = f'https://api.jikan.moe/v4/characters?q={query}&order_by=favorites&sort=desc&page=1'
    search_result = jikanjson(url)
    data = search_result['data']
    data_len = len(search_result['data'])
    if data_len == 1:
      n = 0 
    elif data_len == 0:
      await ctx.send('No results for query.')
      return
    else:
      output = results(data,'name',name,'characters')
      output_message = await ctx.send(output)
      selection_result = await selection(self,ctx,output_message,data_len,'character')
      if selection_result:
        n = selection_result - 1
      else:
        return
        

    search = search_result['data'][n]
    char_about = search['about']

    if len(char_about)>4000:
      message = await ctx.send('Too much information about this character. Slicing the info till 4000 words <a:bot_loading:869160757546340394> ')
      char_about= char_about[:3900]
      await asyncio.sleep(6)
      embed=discord.Embed(title=search['name'], url=search["url"] , description=char_about+'...', color=0x8a7bff)
      embed.add_field(name='Member Favorites',value=search['favorites'], inline= False)
      embed.set_image(url=search['images']['jpg']['image_url'])
      await message.delete()
      await ctx.send(embed=embed)
    else:
      char_about = char_about
      embed=discord.Embed(title=search['name'], url=search["url"] , description=char_about, color=0x8e37b0)
      embed.add_field(name='Member Favorites',value=search['favorites'], inline= False)
      embed.set_image(url=search['images']['jpg']['image_url'])
      await ctx.send(embed=embed)
  
  @character.error
  async def char_error(self,ctx,error):
    if isinstance(error,(MissingRequiredArgument)):
      if ctx.guild:
        await ctx.send('Please provide a query.')
      else:
        return
  
  help_command = f'`{prefix}images Mikasa Ackerman`\n`{prefix}image Lelouch`\n`{prefix}im Eru Chitanda `\n`{prefix}im Midoriya Izuku`\n~~`{prefix}im your mom`~~'
  desc = 'Fetch images for a particular character from anime or manga via '+ '[MyAnimeList](https://myanimelist.net/).'

  @commands.command(name='images',no_pm=True,aliases=['im','image'],brief='Get images for a character from an anime or manga.',usage=f'`{prefix}images <name>`\n`{prefix}image <name>`\n`{prefix}im <name>`',description=desc,help=help_command)
  async def images(self,ctx,*,name):
    if ctx.guild:
      pass
    else:
      return

    if name == 'your mom':
      await ctx.send('https://pbs.twimg.com/media/EUOBhctUEAAWWJj.jpg')
      return

    query = getname(name)
    url = f'https://api.jikan.moe/v4/characters?q={query}&order_by=favorites&sort=desc&page=1'
    search_result = jikanjson(url)
    data = search_result['data']
    data_len = len(search_result['data'])
    if data_len == 1:
      n = 0 
    elif data_len == 0:
      await ctx.send('No results for query.')
      return
    else:
      output = results(data,'name',name,'characters')
      output_message = await ctx.send(output)
      selection_result = await selection(self,ctx,output_message,data_len,'character')
      if selection_result:
        n = selection_result - 1
      else:
        return

    search = search_result['data'][n]
    characterid = search['mal_id']
    char_pictures = jikanjson(f'https://api.jikan.moe/v4/characters/{characterid}/pictures')
    pic_len = len(char_pictures['data']) 
    pic_list = [] 
    for i in range(0,pic_len):
      pic_list.append(char_pictures['data'][i]['large_image_url'])
    len_half = int(len(pic_list)/2)
    
    pictures_list = pic_list[0:len_half]
    pictures_len = len(pictures_list)
    embed_list = []
  
    for i in range(0,len(pictures_list)):
      embed1=discord.Embed(title=search['name'],color=0x8a7bff,description='__Favorites__ : '+str(search['favorites']))
      embed1.set_image(url=pic_list[i])
      embed1.set_footer(text=f'{i+1} / {pictures_len}')
      embed_list.append(embed1)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('🔐', "lock")
    await paginator.run(embed_list)


  @images.error
  async def image_error(self,ctx,error):
    if isinstance(error,(MissingRequiredArgument)):
      if ctx.guild:
        await ctx.send('Please provide a query.')
      else:
        return
  
def setup(bot):
  bot.add_cog(Character_Info(bot))
