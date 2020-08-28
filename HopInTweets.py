from tweepy import *
import time
import config

auth = OAuthHandler(config.cKey, config.cKeySecret)
auth.set_access_token(config.aToken, config.aTokenSecret)
api = API(auth)

class MyStreamListener(StreamListener):

    def on_status(self, status):
        api.retweet(status.id)
        time.sleep(2)


def main():
    myStream = streaming.Stream(auth=api.auth, listener = MyStreamListener())
    myStream.filter(track = ["charity", "donation", "non profits"])


if __name__ == "__main__":
    main()

    
