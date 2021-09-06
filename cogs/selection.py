import asyncio

"""A function that allows users to select the desired name from the matching results.

"""


async def selection(self,ctx,message,data_len,type):
  def check(m):
    return m.author == ctx.author and m.channel == ctx.channel
      
  while True:
    try:
      msg = await self.client.wait_for('message',check=check,timeout=20)
    except asyncio.TimeoutError:
      await ctx.send("Sorry, you didn't reply in time!")
      return None
        
    if msg.content.isdigit():
      if int(msg.content) in [*range(1,data_len+1)]:
        await message.delete()
        await msg.delete()
        return int(msg.content)
      else:
        continue    
    elif msg.content.lower() == 'c':
      await message.delete()
      await msg.delete()
      await ctx.send(f'{ctx.author.name} cancelled the {type} selection.')
      return None
    else:
      continue
      

