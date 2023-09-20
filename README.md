# About
This repository is for a dockerized bot hosted on AWS that interacts with a disc golfing forum. Using data I collected, it classifies posts with a decision tree, and congratulates users when it detects they have made a post celebrating a hole-in-one. It also responds to some comments directed at it.

## More Information Coming Soon

This project is finished and fully working, but I would like to add more information about how to make this and do a pass for code quality soon. 

Unfortunately, a lot of the stuff going on with this project is happening in AWS, potentially making it tricky to make sense of what is here in GitHub without further context.

## Tools used
* AWS - Uses a Lambda function scheduled to run a container hosted in ECR at regular intervals using EventBridge, and communicates with an S3 bucket using boto3
* PRAW (Python Reddit API Wrapper)  
* pandas  
* scikit-learn  
* Docker  

## Learn more
Here are some links I found helpful:  
* https://shpals.medium.com/create-aws-lambda-from-ecr-docker-image-and-integrate-it-with-github-ci-cd-pipeline-dfa3015b5ee0  
* https://new.pythonforengineers.com/blog/build-a-reddit-bot-part-1/  
* https://datagy.io/sklearn-decision-tree-classifier/

