import praw
import pandas as pd

reddit = praw.Reddit("bot")
subreddit = reddit.subreddit("discgolf")

post_values = { 
    # We will collect the following data from each post and represent these data points with a 1 or 0.
    # I have chosen these points pretty arbitrarily and this might not really be enough information to be successful, it is just for learning
        "Start Of Title": [],
        "Ace In Title": [],
        "Ace In Self Text": [],
        "Question In Title": [],
        "Question In Self Text": [],
        "Tagged As Ace": [],
        "Is an Ace Post": [] # This is the value we are trying to predict
    }

for submission in subreddit.new(limit=1000): # This will iterate through the 1000 most recent posts on the subreddit
    
    print("Title: ", submission.title[0:9])

    post_values["Start Of Title"].append(submission.title[0:9])

    if(("ace" or "hole in one") in submission.title.lower()):
        print("Title contains ace")
        post_values["Ace In Title"].append(1)
    else:
        post_values["Ace In Title"].append(0)

    if(("ace" or "hole in one") in submission.selftext.lower()):
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

# If you are following along, you might need to do drop some values or do other work to make sure your data is good at this point
df = pd.DataFrame(post_values)
df.to_csv("data.csv", mode="w", header=False)