#This script runs the bot
#It will check the subreddit for new posts and comments
#If it finds a post that the ml model determines to be an ace, it will reply to it
#It also checks if users comment !info or !stats on its comments, and replies with further information
import praw
import pandas as pd
import joblib
import numpy

model = joblib.load("model.joblib")

reddit = praw.Reddit("bot")
subreddit = reddit.subreddit("discgolf")
#for submission in subreddit.stream.submissions():
for submission in subreddit.new(limit=50):
    print("Processing post with title: ", submission.title)
    post_values = {
        "Ace In Title": 0,
        "Ace In Self Text": 0,
        "Question In Title": 0,
        "Question In Self Text": 0,
        "Tagged As Ace": 0
    }
    if(("ace" or "hole in one") in submission.title.lower() and ("place" or "race" not in submission.title.lower())): #Since the string "ace" is in the words "place" and "race" I decided just to throw them out. This isn't perfect, but it will work for our purposes
        print("Title contains ace")
        post_values["Ace In Title"] = 1

    if(("ace" or "hole in one") in submission.selftext.lower() and ("place" or "race" not in submission.title.lower())):
        print("Text contains ace")
        post_values["Ace In Self Text"] = 1

    if(("?" or "does anyone") in submission.title.lower()):
        print("Title contains question")
        post_values["Question In Title"] = 1

    if(("?" or "does anyone") in submission.selftext.lower()):
        print("Text contains question")
        post_values["Question In Self Text"] = 1

    if("Ace" == submission.link_flair_text):
        print("Tagged as Ace\n")
        post_values["Tagged As Ace"] = 1
    new_data = numpy.array([post_values["Ace In Title"], post_values["Ace In Self Text"], post_values["Question In Title"], post_values["Question In Self Text"], post_values["Tagged As Ace"]]).reshape(1, -1)
    category = model.predict(new_data)
    if(category == 1):
        submission.reply("Congratulations on your ace!")
        print("Replied to post with title: ", submission.title)
        #submission.reply('Congratulations on your ace!\n\nI am a bot, and this comment was made automatically. To view some basic statistics I have collected, reply to this comment with "!stats". To learn more about me, reply to this comment with "!info". If this post was not made to celebrate an ace, please reply to this comment with "bad bot".')