import req as r



class post():
  
  def __init__(self, subreddit='', announce=[]):
    self.posts = []
    self.sub = subreddit
    self.announce = announce 
  
  def get_post(self):
    self.posts.clear()
    left = r.db["lim"]
    while True:
      for submission in r.reddit.subreddit(self.sub).hot(limit=left):
        if submission.id in self.announce or submission.link_flair_text == 'ANNOUNCEMENT':
          #or submission.is_self:
          self.announce.append(submission.id)
          continue
        self.posts.append(submission)
        left -= 1
      if left < 0:
        continue
      break
  
  def check_posts(self):
    plen = 0
    for post in self.posts:
      if post == 'used':
        plen += 1
    if plen == len(self.posts):
      self.posts.clear()
      self.get_post()

  async def send_posts(self, message):
    try:
      number = int(message.content.split() [1]) 
      if number > 100:
        number = 100 
      sent = 0
      while True:
        for i in range(number):
          while True:
            x = r.random.randrange(len(self.posts))
            if self.posts[x] == 'used':
              continue
            break
          if self.posts[x].over_18:
            await message.channel.send('_bonk_ go to horny jail')
            await message.channel.send('This post flagged nsfw')
          else:
            #await message.channel.send('**{}**'.format(str(self.posts[x].title)))
            #if self.posts[x].is_self:
            #  text = message.channel.send(self.posts[x].selftext)
            #if len(self.posts[x].selftext) < 0:  
            #  text = message.channel.send(self.posts[x].selftext)
            #else:
            #  text = None
            embed = r.discord.Embed(title=self.posts[x].title, url = (r.reddit.config.reddit_url + self.posts[x].permalink), color=r.discord.Colour.purple(), description=self.posts[x].selftext)

            if self.posts[x].url[8] == 'i':
              embed.set_image(url=self.posts[x].url)
            footer = r.emoji.emojize(':thumbs_up: {} | :speech_balloon: {}'.format(self.posts[x].score, self.posts[x].num_comments))
            embed.set_footer(text=footer)

            await message.channel.send(embed=embed)  
              #await message.channel.send(self.posts[x].url)

            
              
            
            
            #await message.channel.send(embed)
            sent += 1
            self.posts[x] = 'used'
            self.check_posts()
            await r.asyncio.sleep(1)
        if sent < number:
          number -= sent
          continue  
        break     
    except: 
      x = await message.channel.send("Error")
      await r.asyncio.sleep(5)
      await x.delete()
  
