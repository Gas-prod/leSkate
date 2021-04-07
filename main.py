import os
from os import environ
import tweepy

def auth():

    consumer_key = environ["CONSUMER_KEY"]
    consumer_secret = environ["CONSUMER_SECRET"]

    access_token = environ["ACCESS_TOKEN"]
    access_token_secret = environ["ACESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api,auth


from tweepy.streaming import StreamListener
import time
import json


class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):

        tweet = json.loads(data)
        id_tweet = tweet["id_str"]

        if not tweet["text"].startswith("@") and not tweet["is_quote_status"] and not tweet["text"].startswith("RT @"):
            api.retweet(id_tweet)

api, auth = auth()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track = ["skateboard", "skate", "skateur", "skates", "skater", "kickflip", "heelflip", "shov it", "skatos", "skateshop", "skatepark", "@aureliengiraud", "@Lask8boarderie", "@josephgarbaccio", "@redbullskate", "@biomeskateboard", "@rockslideshop", "@EDYNEclothing", "@vansskate", "@BrailleSkate"], languages=["fr"])
