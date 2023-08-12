import praw

reddit = praw.Reddit("bot")
subreddit = reddit.subreddit("discgolf")
for submission in subreddit.new(limit=150):
    print("Title: ", submission.title)
    if(("ace" or "hole in one") in submission.title.lower() and ("place" not in submission.title.lower())):
        print("Title contains ace")
    if(("ace" or "hole in one") in submission.selftext.lower() and ("place" not in submission.title.lower())):
        print("Text contains ace")
    if(("?" or "does anyone") in submission.title.lower()):
        print("Title contains question")
    if(("?" or "does anyone") in submission.selftext.lower()):
        print("Text contains question")
    if("Ace" == submission.link_flair_text):
        print("Tagged as Ace")