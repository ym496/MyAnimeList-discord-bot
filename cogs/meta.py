import discord
from discord.ext import commands
from discord.errors import Forbidden
async def send_embed(ctx, embed):
  try:
    await ctx.send(embed=embed)
  except Forbidden:
    return

prefix = '+'


class Help(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='help',brief='Shows this message.',description='Shows detailed usage information for the requested command or sends you the general help message.',usage=f'`{prefix}help`\n`{prefix}help <cmd>`',help=f'`{prefix}help`\n`{prefix}help anime`\n`{prefix}help char`',aliases=['list'])
  async def help(self, ctx, *input):
    prefix = '+'
    owner = 'WildCyclotron#0002'
    if not input:
      emb = discord.Embed(title='Commands', color=discord.Color.blue(),description=f'Use `{prefix}help <cmd>` to gain more information about that Command. \n')
      
      module_list = []
      for cog in self.bot.cogs:
        module_list.append(f'{cog}')
      new_module_list = []
      for k in range(0,len(module_list)):
        new_module_list.append(module_list[k].replace('_',' '))
      for i in range(0,len(module_list)):
        command = self.bot.get_cog(module_list[i]).get_commands()
        
        values = []
        for j in range(0,len(command)):
          if not command[j].hidden:
            name = command[j].name
            help_value = command[j].brief
            values.append(f'`{prefix}{name}:` {help_value}')

        emb.add_field(name=new_module_list[i], value='\n'.join(values), inline=False)
      emb.add_field(name="About", value=f"This Bot was developed by {owner}, written in discord.py.")

    elif len(input) == 1:
      module_list = []
      for cog in self.bot.cogs:
        module_list.append(f'{cog}')
      commands_list =[]
      for i in range(0,len(module_list)):
        command = self.bot.get_cog(module_list[i]).get_commands()
        for j in range(0,len(command)):
          commands_list.append(command[j])

      for i in range(0,len(commands_list)):
        name = commands_list[i].name
        command_aliases = commands_list[i].aliases
        if name.lower() == input[0].lower() or input[0].lower() in command_aliases:
          if len(command_aliases) == 0:
            title = f'`{name}`' + ' command documentation. ' 
            emb = discord.Embed(title=title,description='',color=discord.Color.green())
          else:
            aliases = ', '.join(command_aliases)
            title = f'`{name}`' + ' command documentation. ' + f'(Aliases: `{aliases}`)' 
            emb = discord.Embed(title=title,description='',color=discord.Color.green())
          
          emb.add_field(name='Usage', value='\u200b'+commands_list[i].usage, inline=False)
          emb.add_field(name='Description', value=commands_list[i].description, inline=False)
          emb.add_field(name='Examples', value=commands_list[i].help, inline=False)

          break
            
      else:
        emb = discord.Embed(title='',description=f"Command `{input[0]}` not found! \n Use `{prefix}help` to view the list of commands.",color=0xce503e)

        
    elif len(input) > 1:
      user_input = ' '.join(input)
      emb = discord.Embed(title='',description=f'Command `{user_input}` not found!\n Use `{prefix}help` to view the list of commands.',color=0xce503e)
    else:
      pass
                                  
                                


    await send_embed(ctx, emb)


def setup(bot):
    bot.add_cog(Help(bot))
