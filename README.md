# discgolf-reddit-bot
This repository is for a dockerized bot hosted on AWS that interacts with a disc golfing forum. Using data I collected, it classifies posts with a decision tree, and congratulates users when it detects they have made a post celebrating a hole-in-one. The bot shares statistics and interacts with users at their request.
## Tools used
PRAW (Python Reddit API Wrapper)  
pandas  
scikit-learn  
Docker  
AWS - Uses a Lambda function scheduled to run at regular intervals, and communicates with an S3 bucket using boto3   
## Learn more
Here are some links I found helpful:  
https://shpals.medium.com/create-aws-lambda-from-ecr-docker-image-and-integrate-it-with-github-ci-cd-pipeline-dfa3015b5ee0  
https://new.pythonforengineers.com/blog/build-a-reddit-bot-part-1/  
https://datagy.io/sklearn-decision-tree-classifier/

