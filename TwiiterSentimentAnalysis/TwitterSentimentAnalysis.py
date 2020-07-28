from tweepy import Cursor
from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credintials
##Authenticator
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credintials.CONSUMER_KEY, twitter_credintials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credintials.ACCESS_TOKEN, twitter_credintials.ACCESS_TOKEN_SECRET)
        return auth

##STREAMER
class TwitterStreamer():
    def __init__(self,):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self,fetched_tweets_filename, hash_tag_list):
        listener = TwitterListener(fetched_tweets_filename)
        ##authenticator
        auth = self.twitter_authenticator.authenticate_twitter_app()
        ##listener object
        stream = Stream(auth, listener)  ##listener object
        ##Filter
        stream.filter(track=hash_tag_list)
##Listener
class TwitterListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            ##print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print('Error on data: %s' %str(e))
        return true

    def on_error(self, status):
        ##REQ LIMIT
        if status == 420:
            print('Keep the request limit in mind!!')
        print(status)

class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
    def get_user_timeline_tweets(self, num_of_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_of_tweets):
            tweets.append(tweet)
        return tweets

    # def get_friend_list(self, num_friends):
    #     friend_list = []

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id = self.twiiter).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


##MAIN
if __name__ == "__main__":
    hash_tag_list = ['modi ji', 'Modi ji', 'BJP', 'India', 'Covid-19', 'Economy', 'Bharat', 'AAP', 'Arvind Kejriwal']
    fetched_tweets_filename = "tweets.txt"
    twitter_client = TwitterClient('Xooper1')
    twitter_client.get_user_timeline_tweets(1)
    print(twitter_client.get_user_timeline_tweets(1))
    ##to read better converting to json type

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
