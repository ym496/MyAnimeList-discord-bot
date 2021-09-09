from cogs.getjson import jikanjson

"""To send embeds of lists of animes/mangas of the requested status."""

async def userstatus(ctx,name,url,status,bigstatus,type,title):
  try:
    user_status = jikanjson(url)
  except:
    await ctx.send(f"{name}'s list is not public :smiling_face_with_tear: ")
    return
  user_list = user_status[type]
  if len(user_list)> 15:
    await bigstatus(ctx,user_list,title)
  elif len(user_list) == 0:
    await ctx.send(f'Nothing found in their {title} list.')
  else:
    await status(ctx,user_list,title)
