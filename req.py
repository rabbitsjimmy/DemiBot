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

retricted_channels = []

sub_dict = {}
