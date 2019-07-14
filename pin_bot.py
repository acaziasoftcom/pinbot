import discord

client = discord.Client()
THRESHOLD = 5

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')


@client.event
async def on_server_join(server):
  return await client.send_message(
    server.default_channel,
    """ Just add reaction of 📌, and the message pinned! """
  )

@client.event
async def on_reaction_add(reaction, user):
  if str(reaction.emoji) == "📌" and reaction.count >= THRESHOLD:
    print(reaction.message.content)
    await reaction.message.pin()


@client.event
async def on_reaction_remove(reaction, user):
  test_length = list(filter(lambda n:str(n.emoji) == "📌", reaction.message.reactions))
  if len(test_length) < THRESHOLD:
    await reaction.message.unpin()
  # if reaction.emoji == "📌":
  #   if not ":pushpin:" in [reaction.emoji for reaction in reaction.message.reactions]:
  #     await reaction.message.unpin()


if __name__ == '__main__':
  client.run('YOUR_KEY_HERE')
