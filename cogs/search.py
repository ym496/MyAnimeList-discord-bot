import discord
from discord.ext import commands

from discord.ext.commands import MissingRequiredArgument
from cogs.getjson import jikanjson
from cogs.getname import getname
from cogs.results import results
from cogs.selection import selection
prefix = '+'


class Search(commands.Cog):
  def __init__(self, client):
    self.client = client
  description = 'Gives information about any anime via '+ '[MyAnimeList](https://myanimelist.net/).'

  @commands.command(name='anime',brief='Get information about an anime.',usage=f'`{prefix}anime <name>`',help=f'`{prefix}anime Hyouka`\n`{prefix}anime NHK ni Youkoso!`\n`{prefix}anime オレンジ`',description=description)
  async def anime(self,ctx,*,name):
    if ctx.guild:
      pass
    else:
      return
    
    query = getname(name)
    url = f'https://api.jikan.moe/v4/anime?q={query}&order_by=members&sort=desc&page=1'
    search_result = jikanjson(url)
    data = search_result['data']
    data_len = len(search_result['data'])
    if data_len == 1:
      n = 0 
    elif data_len == 0:
      await ctx.send('No results for query.')
      return
    else:
      output = results(data,'title',name,'animes')
      output_message = await ctx.send(output)
      selection_result = await selection(self,ctx,output_message,data_len,'anime')
      if selection_result:
        n = selection_result - 1
      else:
        return
      
    search = search_result["data"][n]
    embed=discord.Embed(title=search["title"], url=search["url"] , description=search['synopsis'], color=0xf37a12)
    embed.set_thumbnail(url=search["images"]['jpg']['image_url'])
    embed.add_field(name="Score", value=search["score"], inline=True)
    embed.add_field(name="Members", value=search["members"], inline=True)
  
    if search["aired"]["from"] is None:
      embed.add_field(name="Start Date", value='Unknown', inline=True)
    else:
      embed.add_field(name="Start Date", value=search["aired"]["from"][:-15], inline=True)
    if search["aired"]["to"] is None:
      embed.add_field(name="End Date", value="Unknown", inline=True)
    else:
      embed.add_field(name="End Date", value=search["aired"]["to"][:-15], inline=True)
  
    embed.add_field(name="Total Episodes", value=search["episodes"], inline=True)
    embed.add_field(name="Type", value=search["type"], inline=True)
    genre = search['genres']
    c = []
    
    for length in range(0,len(genre)):
      c.append(genre[length]['name'])
    
    string = ', '.join([str(item) for item in c])
    genres = string
    embed.add_field(name="Genres", value=genres, inline=False)
    await ctx.send(embed=embed)

  @anime.error
  async def anime_error(self,ctx,error):
    if isinstance(error,(MissingRequiredArgument)):
      if ctx.guild:
        await ctx.send('Please provide a query.')
      else:
        return
  

  desc = 'Gives information about any manga via '+'[MyAnimeList](https://myanimelist.net/).'
  @commands.command(name='manga',brief='Get information about a manga.',usage=f'`{prefix}manga <name>`',description=desc,help=f'`{prefix}manga Omniscient Reader`\n`{prefix}manga attack on titan`\n`{prefix}manga 東京卍リベンジャーズ`')
  async def manga(self,ctx,*,name):
    if ctx.guild:
      pass
    else:
      return

    query = getname(name)
    url = f'https://api.jikan.moe/v4/manga?q={query}&order_by=members&sort=desc&page=1'
    search_result = jikanjson(url)
    
    data = search_result['data']
    data_len = len(search_result['data'])
    if data_len == 1:
      n = 0 
    elif data_len == 0:
      await ctx.send('No results for query.')
      return
    else:
      output = results(data,'title',name,'mangas')
      output_message = await ctx.send(output)
      selection_result = await selection(self,ctx,output_message,data_len,'manga')
      if selection_result:
        n = selection_result - 1
      else:
        return

    search = search_result["data"][n]
    embed=discord.Embed(title=search["title"], url=search["url"] , description=search['synopsis'], color=0xf37a12)
    embed.set_thumbnail(url=search["images"]['jpg']['image_url'])
    
    embed.add_field(name="Score", value=search["scored"], inline=True)
    
    embed.add_field(name="Members", value=search["members"], inline=True)
    
    if search["published"]["from"] is None:
      embed.add_field(name="Start Date", value='Unknown', inline=True)
    else:
      embed.add_field(name="Start Date", value=search["published"]["from"][:-15], inline=True)
    
    if search["published"]["to"] is None:
      embed.add_field(name="End Date", value="Unknown", inline=True)
    else:
      embed.add_field(name="End Date", value=search["published"]["to"][:-15], inline=True)
  
    embed.add_field(name="Total Chapters", value=search["chapters"], inline=True)
    embed.add_field(name="Type", value=search["type"], inline=True)
    genre = search['genres']
    c = []
    for length in range(0,len(genre)):
      c.append(genre[length]['name'])
    string = ', '.join([str(item) for item in c])
    genres = string
  
    embed.add_field(name="Genres", value=genres, inline=False)

    await ctx.send(embed=embed)
  
  @manga.error
  async def manga_error(self,ctx,error):
    if isinstance(error,(MissingRequiredArgument)):
      if ctx.guild:
        await ctx.send('Please provide a query.')
      else:
        return
  

def setup(bot):
  bot.add_cog(Search(bot))
