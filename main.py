import praw

reddit = praw.Reddit("bot")
subreddit = reddit.subreddit("discgolf")
for submission in subreddit.new(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")