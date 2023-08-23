import praw
import pandas as pd

reddit = praw.Reddit("bot")
subreddit = reddit.subreddit("discgolf")

post_values = { 
    #We will collect the following data from each post and represent these data points with a 1 or 0.
    #I have chosen these points pretty arbitrarily, but I think they will be all that is needed to sucessfully determine if the post is celebrating a hole in one.
    #If you want to make your project more sophisticated, you could take this same idea but use a more scientific approach to building a model
    #Another good expansion would be to incorporate some natural language processing to determine the sentiment of the text in the post
        "Start Of Title": [],
        "Ace In Title": [],
        "Ace In Self Text": [],
        "Question In Title": [],
        "Question In Self Text": [],
        "Tagged As Ace": [],
        "Is an Ace Post": [] #This is the value we are trying to predict - this program will set them all to zero and I will go through and manually set the posts that are about aces to 1
    }

for submission in subreddit.new(limit=1000): #This will iterate through the 1000 most recent posts on the subreddit
    
    print("Title: ", submission.title[0:9])

    post_values["Start Of Title"].append(submission.title[0:9])

    if(("ace" or "hole in one") in submission.title.lower() and ("place" or "race" not in submission.title.lower())): #Since the string "ace" is in the words "place" and "race" I decided just to throw them out. This isn't perfect, but it will work for our purposes
        print("Title contains ace")
        post_values["Ace In Title"].append(1)
    else:
        post_values["Ace In Title"].append(0)

    if(("ace" or "hole in one") in submission.selftext.lower() and ("place" or "race" not in submission.title.lower())):
        print("Text contains ace")
        post_values["Ace In Self Text"].append(1)
    else:
        post_values["Ace In Self Text"].append(0)

    if(("?" or "does anyone") in submission.title.lower()):
        print("Title contains question")
        post_values["Question In Title"].append(1)
    else:
        post_values["Question In Title"].append(0)

    if(("?" or "does anyone") in submission.selftext.lower()):
        print("Text contains question")
        post_values["Question In Self Text"].append(1)
    else:
        post_values["Question In Self Text"].append(0)

    if("Ace" == submission.link_flair_text):
        print("Tagged as Ace\n")
        post_values["Tagged As Ace"].append(1)
    else:
        post_values["Tagged As Ace"].append(0)
    post_values["Is an Ace Post"].append(0)

#For your purposes, you may need to drop rows with empty values or do some other work
df = pd.DataFrame(post_values)
df.to_csv("data.csv", mode="w", header=False)