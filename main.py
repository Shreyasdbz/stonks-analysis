#! usr/bin/env python3
import os
import datetime as dt
from dotenv import load_dotenv
import pandas as pd
import praw
import csv

load_dotenv()

topics_dict = { "title":[], 
                "score":[], 
                "id":[], "url":[], 
                "comms_num": [], 
                "created": [], 
                "body":[] }

reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), 
                     client_secret=os.getenv('CLIENT_SECRET'), 
                     user_agent=os.getenv('USER_AGENT'))

subreddit = reddit.subreddit('Robinhood')
top_subreddit = subreddit.top()

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('data/testResults.csv', index=False) 
