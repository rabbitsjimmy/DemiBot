import req as r
import classes as c



def get_quote():
  response = r.requests.get("https://zenquotes.io/api/random")
  json_data = r.json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in r.db.keys():
    encouragements = r.db["encouragements"]
    encouragements.append(encouraging_message)
    r.db["encouragements"] = encouragements
  else:
    r.db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = r.db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  r.db["encouragements"] = encouragements

async def bomb(message):
  text_channel_list = []
  for channel in message.guild.text_channels:
    text_channel_list.append(channel)
  nm = message.content.split()[1]
  await message.delete()
  for channel in text_channel_list:
  #for channel in trial_list:
    x = False
    for thing in r.retricted_channels:
      if channel == r.client.get_channel(thing):
        x = True
        break
    if x:
      x = False
      continue
    try:
      x = await channel.send(nm)
      await x.delete()
    except:
      continue

async def shout(message):
  text_channel_list = []
  for channel in message.guild.text_channels:
    text_channel_list.append(channel)
  nm = ' '.join(message.content.split()[1:])
  await message.delete()
  for channel in text_channel_list:
  #for channel in trial_list:
    x = False
    for thing in r.retricted_channels:
      if channel == r.client.get_channel(thing):
        x = True
        break
    if x:
      x = False
      continue
    try:
      x = await channel.send(nm)
    except:
      continue

async def new_sub(message):
    try:
      sub = message.content.split()[1]
      if r.reddit.subreddit(sub).over18:
        await message.channel.send('*bonk* go to horny jail')
        await message.channel.send('This is an NSFW subreddit')
      else:
        r.sub_dict[sub] = c.post(subreddit=sub)
        await message.channel.send('Subreddit linked')
        r.sub_dict[sub].get_post()
    except:
      await message.channel.send('An Error has occured')
    