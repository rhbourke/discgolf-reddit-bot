#This script runs the bot
#It will check the subreddit for new posts and comments
#If it finds a post that the ml model determines to be an ace, it will reply to it
#It also checks if users comment !info or !stats on its comments, and replies with further information
import praw
import pandas as pd
import joblib

model = joblib.load("model.joblib")

predictions = model.predict([[0, 0, 1, 1, 1]])
print(predictions)
# reddit = praw.Reddit("bot")
# subreddit = reddit.subreddit("discgolf")
# for submission in subreddit.stream.submissions():
#     print("Processing post with title: ", submission.title)
#     post_values = {
#         "Start Of Title": [],
#         "Ace In Title": [],
#         "Ace In Self Text": [],
#         "Question In Title": [],
#         "Question In Self Text": [],
#         "Tagged As Ace": []
#     }
#     if(("ace" or "hole in one") in submission.title.lower() and ("place" or "race" not in submission.title.lower())): #Since the string "ace" is in the words "place" and "race" I decided just to throw them out. This isn't perfect, but it will work for our purposes
#         print("Title contains ace")
#         post_values["Ace In Title"].append(1)
#     else:
#         post_values["Ace In Title"].append(0)

#     if(("ace" or "hole in one") in submission.selftext.lower() and ("place" or "race" not in submission.title.lower())):
#         print("Text contains ace")
#         post_values["Ace In Self Text"].append(1)
#     else:
#         post_values["Ace In Self Text"].append(0)

#     if(("?" or "does anyone") in submission.title.lower()):
#         print("Title contains question")
#         post_values["Question In Title"].append(1)
#     else:
#         post_values["Question In Title"].append(0)

#     if(("?" or "does anyone") in submission.selftext.lower()):
#         print("Text contains question")
#         post_values["Question In Self Text"].append(1)
#     else:
#         post_values["Question In Self Text"].append(0)

#     if("Ace" == submission.link_flair_text):
#         print("Tagged as Ace\n")
#         post_values["Tagged As Ace"].append(1)
#     else:
#         post_values["Tagged As Ace"].append(0)
#     post_values["Is an Ace Post"].append(0)