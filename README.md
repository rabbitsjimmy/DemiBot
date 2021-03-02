# DemiBot
A discord bot made for fun and memes

All of the code here is my own except for the discord message sensor which sends encouragements, that is from an article I found about making a discord bot and helped start this entire project.


main.py: houses all of the commands for the bot, it is lacking a help command 
classes.py: currently only contains code for connecting to any subreddit and scraping/ sending posts to discord setup in a class system
funcs.py: miscellaneous functions which are stored in there to make main.py shorter
keep_alive.py: sets up a webserver with flask and using uptimerobot the repl will never shut down
req.py: various python modules and a universal initialization of reddit and discord instances, as well as some channels that were manually added that the bot would not talk in.



The main use of the bot is to improve upon the dankmemer discord bot. It was made without looking at that code (I don't know js anyway so) and works by $create subreddit and then $subreddit #of posts you want

It does a few other things like ghost pinging in every text channel on the discord server.

It is run on repl.it and on there it has a .env file which contains the bot token, reddit script id, and reddit script secret which looks like this:
TOKEN = discord bot token
Rid = reddit script id
RSec = reddit script sec

In order to run the bot an apllication must be created with discord AND a script must be created with reddit

Make sure to fill in the user_agent in req.py as that shows reddit who you are. Basically just put something in the string like 'Name of bot, version, by /u/redditusername
