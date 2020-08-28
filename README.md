# HopInTwitterBot

A twitter bot that uses the Twitter API to stream and retweet tweets about charity. See it in action at hopincharity.com!

## Set up

1. If you don't already have a twitter account, create one (twitter.com).
2. Go to developer.twitter.com and sign up your app to get API keys.
3. Clone this repository

```shell
git clone https://github.com/sambluestone/HopInTwitterBot.git
```

4. Create a file in the root directory called config.py and format it in the following way:
   <pre>
   cKey = "xxxxxxxxxxxxxxxxxxxxxxxxx"
   cKeySecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   aToken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   aTokenSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   <pre>
Note: make sure that each key is surrounded by double quotes and the variables are named appropriately


5. Install the tweepy client library

```shell
pip install tweepy
```

## Usage

Run hopInTweets.py in your IDE (if possible) or from the command line by running

```shell
 python hopInTweets.py
```
