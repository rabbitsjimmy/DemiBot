import discord
import os
import requests
import json
import random
from replit import db
import asyncio
import praw
import emoji
#import sr_api



client = discord.Client()

reddit = praw.Reddit(
  client_id=os.getenv("Rid"),
  client_secret=os.getenv('RSec'),
  user_agent=""
)

retricted_channels = [572111005652484116, 549771607510351873, 667590171553824788, 431199184532668416, 620412060567601152, 687430176296009764, 431229881146408969, 643938912028590114, 753257580721209435, 643939000276615182, 438129056207077377]

sub_dict = {}
