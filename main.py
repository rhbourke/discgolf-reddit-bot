#This script runs the bot
#It will check the subreddit for new posts and comments
#If it finds a post that the ml model determines to be an ace, it will reply to it
#It also checks if users comment !info or !stats on its comments, and replies with further information
import praw

reddit = praw.Reddit("bot")
subreddit = reddit.subreddit("discgolf")
for submission in subreddit.stream.submissions():
    print("Title: ", submission.title)