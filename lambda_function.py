# This script runs the bot
# It will check the subreddit for new posts and comments
# If it finds a post that the ml model determines to be an ace, it will reply to it
# It also checks if users comment !info or !stats on its comments, and replies with further information
import datetime
import praw
import pandas as pd
import joblib
import numpy
import records
import boto3
def lambda_handler(event, context):

        
    model = joblib.load("model.joblib")

    # Load data from past runs from AWS S3
    s3 = boto3.client('s3')
    bucket_name = "redditdiscgolfbotstorage"
    records_key = "records.joblib"
    s3.download_file(bucket_name, records_key, "/tmp/records_file")
    recordsBook = joblib.load("/tmp/records_file")
    print("Loaded records book from S3.")

    reddit = praw.Reddit("bot")
    subreddit = reddit.subreddit("discgolf")

    for submission in subreddit.new(limit=20):
        if(submission.created_utc <= recordsBook.last_post_time): # We only want to process posts that were created after the last time we ran the bot
            break
        print("Processing post with title: ", submission.title)
        post_values = {
            "Ace In Title": 0,
            "Ace In Self Text": 0,
            "Question In Title": 0,
            "Question In Self Text": 0,
            "Tagged As Ace": 0
        }
        if(("ace" or "hole in one") in submission.title.lower()):
            print("Title contains ace")
            post_values["Ace In Title"] = 1

        if(("ace" or "hole in one") in submission.selftext.lower()):
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
            submission.reply('Congratulations on your ace!\n\nI am a bot, and this comment was made automatically. To view some basic statistics I have collected, reply to this comment with "!stats". To learn more about me, reply to this comment with "!info". If this post was not made to celebrate an ace, please reply to this comment with "bad bot".')
            print("Replied to post with title: ", submission.title)
            recordsBook.add_message(f"Found ace post! Replied to post with title: {submission.title} on {datetime.datetime.now()}")
        recordsBook.add_post_to_data(category)

    for submission in subreddit.new(limit=1): # After processing all the posts, we want to update the last post time to the most recent post
        # We have a tiny chance of missing a post if it was made while the program was in the previous loop, but that is fine for my purposes
        recordsBook.set_last_post_time(submission.created_utc)

    for reply in reddit.inbox.unread():
        print("Processing reply from author: ", reply.author)
        if(reply.body == "!info"):
            reply.reply("""I was programmed using Python and I use a basic machine learning algorithm to classify posts called a decision tree. 
                        I use the PRAW library and am deployed on AWS. I collect statistics about activity in the subreddit that the author plans 
                        to visualize and share someday to benefit the community. I do not collect any personal information.""")
            print("Replied to info comment from author: ", reply.author)
        elif(reply.body == "!stats"):
            reply.reply(f"""So far, I have found {recordsBook.get_ace_post_count()} posts celebrating an ace after analyzing {recordsBook.get_total_post_count()} posts. I have been called a bad bot {recordsBook.get_bad_bot_count()} times.""")
            print("Replied to stats comment from author: ", reply.author)
        elif(reply.body == "bad bot"):
            reply.reply("Sorry, I'm still learning!")
            print("Replied to bad bot comment from author: ", reply.author)
            recordsBook.increment_bad_bot_count()

    reddit.inbox.mark_all_read()

    joblib.dump(recordsBook, "/tmp/records_file")
    s3.upload_file(Bucket=bucket_name, Key=records_key, Filename="/tmp/records_file")
    print("Saved records book to S3.")


if __name__ == "__main__":
    lambda_handler(None, None)
