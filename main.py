import req as r
from keep_alive import keep_alive
import funcs as f
import classes as c



if "lim" not in r.db.keys():
  r.db["lim"] = 150


memes = c.post(subreddit='memes', announce=['ksm802'])
if len(memes.posts) == 0:
  memes.get_post()


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depression", "feeling down", "this bot sucks", "I'm tired", "i'm tired", "im tired", "suck", "sucks", "rip"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You are a great person",
  "Everything gets better"
]

retricted_channels = []



if "responding" not in r.db.keys():
  r.db["responding"] = True

if "lim" not in r.db.keys():
  r.db["lim"] = 150




@r.client.event
async def on_ready():
  print("We have logged in as {0.user}".format(r.client))

@r.client.event
async def on_message(message):
  


  if message.author == r.client.user:
    return


  msg = message.content
  text_channel_list = []
  for channel in message.guild.text_channels:
            text_channel_list.append(channel)
#  trial_list = []
#  for channel in message.guild.channels:
#    #if channel.type == 'text_channel':
#      trial_list.append(channel)


  if msg.startswith("$set limit"):
    try:
      value = int(msg.split("$set limit ",1)[1])
      r.db["lim"] = value
      await message.channel.send("Set meme limit to {}".format(value))
      memes.get_post()
    except:
      await message.channel.send("Invalid Limit")
    
    


  if msg.startswith("$inspire"):
    quote = f.get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
  
  
  if msg.startswith('$snipe'):
        await message.delete()
  
  if msg.startswith('$say'):
    nm = ' '.join(message.content.split()[1:])
    await message.delete()
    await message.channel.send(nm)
  
  if msg.startswith('$bomb'):
    await f.bomb(message)

  if msg.startswith('$shout'):
    await f.shout(message)

  if msg.startswith('$meme'):
    await memes.send_posts(message)


  if msg.startswith('$create'):
    await f.new_sub(message)
  
  for sub in r.sub_dict:
    if msg.startswith('$' + sub):
      await r.sub_dict[sub].send_posts(message)
      break

  if r.db["responding"]:
    options = starter_encouragements
    if "encouragements" in r.db.keys():
      options = options + r.db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(r.random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    f.update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in r.db.keys():
      index = int(msg.split("$del",1)[1])
      f.delete_encouragment(index)
      encouragements = r.db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in r.db.keys():
      encouragements = r.db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      r.db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      r.db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()
r.client.run(r.os.getenv("TOKEN"))

